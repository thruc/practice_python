import requests
# TODO: https://github.com/microsoft/pylance-release/issues/597
# 警告が出る
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import time


def get_html(url):
    with requests.Session() as s:
        retries = Retry(total=5,
                backoff_factor=1,
                status_forcelist=[ 500, 502, 503, 504 ])
        s.mount
        s.mount('https://', HTTPAdapter(max_retries=retries))
        r = s.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def get_data(url):
    return_data = []

    # HTML取得
    soup = get_html(url)

    # 一覧のデータを取得
    items = soup.findAll("div", {"class": "cassetteitem"})

    # 物件の数分ループ
    for item in items:
        base_data = {}

        # 基本情報
        base_data["名称"] = item.find("div", {"class": "cassetteitem_content-title"}).getText().strip()
        base_data["カテゴリー"] = item.find("div", {"class": "cassetteitem_content-label"}).getText().strip()
        base_data["アドレス"] = item.find("li", {"class": "cassetteitem_detail-col1"}).getText().strip()
        base_data["築年数"] = item.find("li", {"class": "cassetteitem_detail-col3"}).findAll("div")[0].getText().strip()
        base_data["構造"] = item.find("li", {"class": "cassetteitem_detail-col3"}).findAll("div")[1].getText().strip()

        # 駅のデータ取得
        stations = item.findAll("div", {"class": "cassetteitem_detail-text"})
        # 駅数分ループ
        station_list = []
        station_list_append = station_list.append
        for station in stations:
            station_list_append(station.getText().strip())

        base_data["アクセス"] = "~".join(station_list)

        # 部屋毎のデータ取得
        rooms = item.find("table", {"class": "cassetteitem_other"}).findAll("tbody")

        for room in rooms:
            data = base_data.copy()

            data["階数"] = room.findAll("td")[2].getText().strip()

            data["家賃"] = room.findAll("td")[3].findAll("li")[0].getText().strip()
            data["管理費"] = room.findAll("td")[3].findAll("li")[1].getText().strip()

            data["敷金"] = room.findAll("td")[4].findAll("li")[0].getText().strip()
            data["礼金"] = room.findAll("td")[4].findAll("li")[1].getText().strip()

            data["間取り"] = room.findAll("td")[5].findAll("li")[0].getText().strip()
            data["面積"] = room.findAll("td")[5].findAll("li")[1].getText().strip()

            data["URL"] = "https://suumo.jp" + room.findAll("td")[8].find("a").get("href")

            return_data.append(data)

    return return_data


if __name__ == "__main__":
    all_data = []
    max_page = 2
    # 一覧画面のURL
    # TODO: 検索条件も変数で管理できるようにする
    base_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&cb=0.0&ct=9999999&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50&page={}"

    for page in range(1, max_page+1):
        url = base_url.format(page)
        all_data += get_data(url)
        time.sleep(1)

    print(all_data)