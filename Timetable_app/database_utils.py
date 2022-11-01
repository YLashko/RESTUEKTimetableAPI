from .models import Timetable, TableRow
from .scraper.timetable_utils import get_table_json
import datetime as dt
import pytz
from .config import UPDATE_DELAY


def save_json_table(json_table: dict):
    if Timetable.objects.filter(group_id=json_table["group_id"]).exists():
        Timetable.objects.filter(group_id=json_table["group_id"]).delete()
    now = pytz.utc.localize(dt.datetime.utcnow())
    table = Timetable.objects.create(
        group_name=json_table["group_name"],
        group_id=json_table["group_id"],
        updated=now
    )
    for row in json_table["table_rows"]:
        save_json_table_row(table, row)


def save_json_table_row(table, table_row: dict):
    date = dt.datetime.strptime(table_row["date"], "%Y-%m-%d")
    time_start = dt.datetime.strptime(table_row["time"][3:8], "%H:%M")
    time_end = dt.datetime.strptime(table_row["time"][11:16], "%H:%M")
    TableRow.objects.create(
        timetable=table,
        date=date,
        start_time=time_start,
        end_time=time_end,
        subject_name=table_row["subject_name"],
        type=table_row["type"],
        professor_name=table_row["professor_name"],
        professor_page_link=table_row["professor_page_link"],
        rescheduled_info=table_row["rescheduled_info"]
    )


def get_table(group_id):
    if update_required(group_id):
        save_json_table(get_table_json(group_id))
        print("scraped database")
    return Timetable.objects.get(group_id=group_id)


def update_required(group_id) -> bool:
    if not Timetable.objects.filter(group_id=group_id).exists():
        return True
    tt = Timetable.objects.get(group_id=group_id)
    print(dt.datetime.utcnow() - tt.updated.replace(tzinfo=None))
    return dt.datetime.utcnow() - tt.updated.replace(tzinfo=None) > UPDATE_DELAY


def rows_to_dict_list(rows: list) -> list[dict]:
    return [obj.dict() for obj in rows]
