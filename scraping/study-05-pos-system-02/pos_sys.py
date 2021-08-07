import os
import datetime
MASTER_FILE = "/".join([os.path.dirname(__file__), "master.csv"])
RECEIPT_DIR = "/".join([os.path.dirname(__file__), "receipt/"])


# 商品クラス
class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price

    def get_price(self):
        return self.price


# オーダークラス
class Order:
    def __init__(self, item_master):
        self.item_order_list = []
        self.item_master = item_master
        self.sum_price = 0
        self.sum_count = 0
        self.change = 0
        self.recieved = 0
        self.sum_deta = {}

    def view_menu(self):
        # メニューを返す
        menu = "<h2>メニュー</h2>"
        for item in self.item_master:
            menu += "{} {} {}円<br>".format(
                item.item_code,
                item.item_name,
                item.price
            )
        return menu

    def create_select(self):
        select = ""
        for item in self.item_master:
            select += '<option value="{0}">{0}</option>'.format(item.item_code)

        return '商品コード：<select name="code" id="code">{}</select>'.format(select)

    def add_item_order(self, item_code, order_num):
        """商品をオーダーリストに追加

        Args:
            item_code (str): 商品コード
            item_num (int): 注文数
        """
        for _ in range(int(order_num)):
            self.item_order_list.append(item_code)

    def check_order_list(self):
        msg = "<h2>注文リスト</h2>"
        self.sum_deta = {}
        self.sum_price = 0
        self.sum_count = 0
        for item_order in self.item_order_list:
            if self.sum_deta.get(item_order) is None:
                self.sum_deta[item_order] = 1
            else:
                self.sum_deta[item_order] += 1

        for code, count in self.sum_deta.items():
            name, price = self.get_item_data(code)
            self.sum_price += price*count
            self.sum_count += count
            msg += "商品コード:{} 商品名:{}     {}個   ￥{}".format(
                code,
                name,
                count,
                price*count
            )
            msg += "<br>"

        # 合計金額、個数の表示
        msg += "<br>"
        msg += "合計金額:￥{} {}個".format(self.sum_price, self.sum_count)
        msg += "<br>"
        return msg

    def get_item_data(self, item_code):
        """
        商品コードに紐付く商品名と値段を取得する

        Args:
            item_code (str): 商品コード

        Returns:
            taple: (商品名, 値段)
        """
        for m in self.item_master:
            if item_code == m.item_code:
                return m.item_name, m.price

    def culc_change(self):
        # おつりを計算する
        self.change = self.recieved - self.sum_price

        if self.change > 0:
            msg = "おつり{}円になります".format(self.change)
            flg = True
        else:
            msg = "お金が足りません"
            flg = False

        return msg, flg

    def export_receipt(self):
        # レシートを発行する
        file_name = RECEIPT_DIR + \
            "{}.txt".format(datetime.datetime.now().strftime('%Y%m%d%H%M'))

        msg = "レシート\n"
        for code, count in self.sum_deta.items():
            name, price = self.get_item_data(code)
            msg += "商品コード:{} 商品名:{}     {}個   ￥{}\n".format(
                code,
                name,
                count,
                price*count
            )

        # 合計金額
        msg += "\n"
        msg += "合計金額:￥{}\n".format(self.sum_price)
        msg += "お預かり:{}円\n".format(self.recieved)
        msg += "おつり:{}円".format(self.change)

        with open(file_name, mode="a", encoding="utf-8_sig") as f:
            f.write(msg)

        return file_name
