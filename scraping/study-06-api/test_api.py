import api
import pandas as pd
import os


class TestApi():
    def test_ichiba_item_search(self):
        keywrod = "きめつ"
        file_name = "kimetu.csv"
        api.ichiba_item_search(keywrod, file_name)
        assert os.path.isfile("./csv/kimetu.csv")

    def test_product_search(self):
        product_id = "484ad5ad36cc16c6cd035d9c5f65e449"
        api.product_search(product_id)
        assert os.path.isfile("./csv/product.csv")

    def test_rank(self):
        genre_id = "566403"
        api.rank(genre_id)
        assert os.path.isfile("./csv/rank.csv")
