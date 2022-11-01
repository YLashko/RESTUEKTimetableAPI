from Timetable_app.scraper.scraper import *
from Timetable_app.scraper.convert import *


def get_table_json(group_id: str) -> dict:
    output = {}
    page = get_page(group_id)
    group_name = page.find("div", {"class": "grupa"})
    output["table_rows"] = tr_list_to_json_list(all_table_rows(extract_table(page)))
    output["group_name"] = group_name.text
    output["group_id"] = group_id
    return output
