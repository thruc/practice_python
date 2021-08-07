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
    #driver.get("https://www.oxfordlearnersdictionaries.com/")
    driver.get("https://www.oxfordlearnersdictionaries.com/")
    e_q = driver.find_element_by_id("q")
    e_q.send_keys(search_keyword)
    e_q.submit()
    #/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div

    e_syn = driver.find_elements_by_xpath("//span[@xt='syn']")
    e_nsyn = driver.find_elements_by_xpath("//span[@xt='nsyn']")
    e_opp = driver.find_elements_by_xpath("//span[@xt='opp']")
    # e_pos
    e_relatedentries = driver.find_element_by_id("relatedentries")
    e_il = e_relatedentries.find_elements_by_tag_name("li")
    print(e_il)

    print(e_syn)
    for s in e_syn:
        print(s.text)

    for n in e_nsyn:
        print(n.text)

    for o in e_opp:
        print(o.text)

    for r in e_il:
        s = r.find_element_by_tag_name("span")
        p = r.find_element_by_tag_name("pos")
        print("{}:{}".format(s.text, p.text))



    time.sleep(10)


if __name__ == "__main__":
    main()
