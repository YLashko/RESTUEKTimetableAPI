from .database_utils import get_table, rows_to_dict_list
import datetime as dt


def get_by_date(group_id: str, date: str):
    date = dt.datetime.strptime(date, "%Y-%m-%d")
    table = get_table(group_id)
    filtered = table.row.filter(date=date)
    return rows_to_dict_list(filtered)


def get_by_date_start_time(group_id: str, date: str, time: str):
    date = dt.datetime.strptime(date, "%Y-%m-%d")
    time = dt.datetime.strptime(time, "%H:%M")
    table = get_table(group_id)
    filtered = table.row.filter(date=date, start_time=time)
    return rows_to_dict_list(filtered)
