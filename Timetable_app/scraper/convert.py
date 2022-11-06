from bs4 import Tag


def tr_list_to_json_list(tr_list: list[Tag]) -> list[dict]:
    tr_json = []
    for tag in tr_list:
        rescheduled = len(tag) == 1
        td_list = tag.find_all("td")
        if not rescheduled:
            professor_name, link = extract_professor_name_and_link(td_list[4])
            tr_json.append({
                "date": td_list[0].getText(),
                "time": td_list[1].getText(),
                "subject_name": td_list[2].getText(),
                "type": td_list[3].getText(),
                "professor_name": professor_name.strip(),
                "professor_page_link": link,
                "rescheduled_info": None,
                "place": td_list[5].getText(),
            })
        else:
            tr_json[-1]["rescheduled_info"] = td_list[0].getText()
    return tr_json


def extract_professor_name_and_link(td_tag: Tag):
    link = td_tag.find_next("a").get("href")
    name = td_tag.getText()
    return name, link
