from itertools import count
import logging
import os
from sys import path
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from selenium.common.exceptions import SessionNotCreatedException
import datetime
import logging

NOW = datetime.datetime.now().strftime('%Y%m%d%H%M')

DIR_PATH = os.path.dirname(__file__)
CSV_FILE_NAME = DIR_PATH + "/csv/{}.csv".format(NOW)
LOG_FILE_NAME = DIR_PATH + "/log/{}.log".format(NOW)

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler(filename=LOG_FILE_NAME, encoding='utf-8'))


### ログファイルおよびコンソール出力
def log(msg):
    # ログ出力
    logger.info(msg)

def print_pro_bar(count_num, all_num, ok, ng):
    """プログレスバーを表示する

    Args:
        count_num (int): 現状で取得しようとした件数
        all_num (int): 検索ワードでヒットした件数
        ok (int): 取得できた件数
        ng (int): 失敗した件数
    """
    pro_par = count_num / all_num * 20.
    pro_bar = ('=' * int(pro_par)) + (' ' * (20 - int(pro_par)))
    per = int(count_num / all_num * 100)

    print('\r[{0}] {1}% "ok{2},ng{3},count{4}'.format(
        pro_bar, per, str(ok), str(ng), str(all_num)), end='')



def set_driver(driver_path, headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    # exe_path = os.getcwd() + "/" + driver_path
    exe_path = os.path.join(DIR_PATH, driver_path)
    try:
        driver = Chrome(executable_path=exe_path, options=options)
    except SessionNotCreatedException:
        # Chromeドライバーがバージョンアップの際に自動で更新されるようにしてみましょう。
        # 参考：https://qiita.com/YoshikiIto/items/000f241f6d917178981c
        driver = Chrome(ChromeDriverManager(path=DIR_PATH).install(), options=options)

    return driver


# main処理
def main():
    search_keyword = input("キーワードを入力してください：")
    # driverを起動
    logger.info("driverを起動")
    if os.name == 'nt':  # Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix':  # Mac
        driver = set_driver("chromedriver", False)
    # Webサイトを開く
    driver.implicitly_wait(5)
    driver.get("https://tenshoku.mynavi.jp/")

    try:
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(5)
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
    except:
        pass

    # 検索窓に入力
    driver.find_element_by_class_name("topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()

    # 取得した情報を格納する辞書のリスト
    cassette_recruit_dict_lsit = []
    list_append = cassette_recruit_dict_lsit.append

    # 現状で取得しようとした件数,取得できた件数,失敗した件数
    count_num, ok, ng = 0, 0, 0

    page_num = 1
    all_num = int(driver.find_element_by_class_name("js__searchRecruit--count").text)

    while True:
        cassetteRecruit_list = driver.find_elements_by_class_name("cassetteRecruit")
        for cassetteRecruit in cassetteRecruit_list:
            try:
                # 取得情報を格納する辞書を初期化
                cassette_recruit_dict = {}
                # 会社名
                cassette_recruit_dict["name"] = cassetteRecruit.find_element_by_class_name(
                    "cassetteRecruit__name").text
                # キャッチコピー
                cassette_recruit_dict["copy"] = cassetteRecruit.find_element_by_class_name(
                    "cassetteRecruit__copy").text
                # 雇用形態
                cassette_recruit_dict["status"] = cassetteRecruit.find_element_by_class_name(
                    "labelEmploymentStatus").text
                # HPのURL
                cassette_recruit_dict["url"] = cassetteRecruit.find_element_by_class_name(
                    "cassetteRecruit__copy").find_element_by_tag_name("a").get_attribute("href")
                # テーブルの内容取得
                tableCondition = cassetteRecruit.find_element_by_class_name("tableCondition")
                tr_list = tableCondition.find_elements_by_tag_name("tr")

                for tr in tr_list:
                    # テーブルのヘッダー
                    t_head = tr.find_element_by_class_name("tableCondition__head").text
                    # テーブルのボディ
                    t_body = tr.find_element_by_class_name("tableCondition__body").text
                    # 取得情報を格納する辞書にキーをヘッダー、値をボディに格納
                    # 仕事内容,対象となる方,勤務地,給与,初年度年収
                    cassette_recruit_dict[t_head] = t_body

                list_append(cassette_recruit_dict)

                ok += 1
                logger.info("{}件目成功".format(count_num))

            except:
                # エラーが発生した場合
                ng += 1
                logger.info("{}件目失敗".format(count_num))
            finally:
                count_num += 1
                # TODO プログレスバー表示したい 現状ログ出力と競合するためコメントアウト
                # print_pro_bar(count_num, all_num, ok, ng)



        try:
            # ２ページ目以降の情報も含めて取得できるようにしてみましょう
            next_link = driver.find_element_by_class_name(
                "iconFont--arrowLeft").get_attribute("href")
            time.sleep(1)
            driver.get(next_link)
            # TODO 取得したいページ数を指定したい
            # if page_num == 2:
            #     break
        except:
            logger.info("ページ取得失敗:{}ページ".format(page_num))
            break
        page_num += 1

    # 取得した結果をCSVファイルに出力
    df = pd.io.json.json_normalize(cassette_recruit_dict_lsit)
    df.to_csv(CSV_FILE_NAME)
    logger.info(f"終了  OK:{ok} NG:{ng}")

if __name__ == "__main__":
    main()
