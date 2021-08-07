import requests
import pandas as pd

CSV_DIR = "./csv/"


def get_api(url):
    result = requests.get(url)
    return result.json()


def ichiba_item_search(keyword, file_name="search.csv"):
    """任意のキーワードでAPIを検索した時の商品名と価格の一覧を取得

    Args:
        keyword (str): 任意のキーワード
    """
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    result_json = get_api(url)
    item_list = result_json["Items"]

    ex_list = []
    for item in item_list:
        ex_dict = {}
        ex_dict["商品名"] = item["Item"]["itemName"]
        ex_dict["価格"] = item["Item"]["itemPrice"]
        ex_list.append(ex_dict)

    df = pd.json_normalize(ex_list)
    df.to_csv(CSV_DIR+file_name)


def product_search(product_id, file_name="product.csv"):
    """任意の商品IDの最安値と最高値を取得

    Args:
        product_id (str): productId　任意の商品ID
    """
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&productId={}&applicationId=1019079537947262807".format(
        product_id)
    result_json = get_api(url)
    product = result_json["Products"][0]["Product"]

    ex_list = []
    ex_dict = {}
    ex_dict["商品名"] = product["productName"]
    ex_dict["最小価格"] = product["minPrice"]
    ex_dict["最大価格"] = product["maxPrice"]
    ex_list.append(ex_dict)

    df = pd.json_normalize(ex_list)
    df.to_csv(CSV_DIR+file_name)


def rank(genreid, file_name="rank.csv"):
    """任意のジャンルIDからランキング一覧を取得

    Args:
        genreid (str): 任意のジャンルID
    """
    ranking_url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&genreId={}&applicationId=1019079537947262807".format(
        genreid)

    result = get_api(ranking_url)
    item_list = result['Items']
    ex_list = []

    for item in item_list:
        ex_dict = {}
        ex_dict["ランキング"] = item['Item']['rank']
        ex_dict["商品名"] = item['Item']['itemName']
        ex_dict["価格"] = item['Item']['itemPrice']
        ex_list.append(ex_dict)
    df = pd.json_normalize(ex_list)
    df.to_csv(CSV_DIR+file_name)


if __name__ == "__main__":
    keyword = "鬼滅"
    product_id = "484ad5ad36cc16c6cd035d9c5f65e449"
    genre_id = "566403"

    ichiba_item_search(keyword)
    product_search(product_id)
    rank(genre_id)
