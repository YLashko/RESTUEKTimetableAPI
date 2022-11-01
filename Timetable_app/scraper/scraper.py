import ssl
import requests
import urllib3
from bs4 import BeautifulSoup, Tag


# found on stackoverflow
class SslOldHttpAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')

        self.poolmanager = urllib3.poolmanager.PoolManager(
            ssl_version=ssl.PROTOCOL_TLS,
            ssl_context=ctx)


def get_page(group_id: str) -> BeautifulSoup:
    request = f"https://planzajec.uek.krakow.pl/index.php?typ=G&id={group_id}&okres=3"
    s = requests.Session()
    s.mount(request, SslOldHttpAdapter())
    r = s.get(request)
    bs = BeautifulSoup(r.content, "html.parser")
    return bs


def extract_table(page_bs: BeautifulSoup) -> BeautifulSoup:
    return page_bs.body.table


def all_table_rows(table_bs: BeautifulSoup) -> list[Tag]:
    return list(table_bs.find_all("tr")[1:])
