import pandas as pd
import os
import datetime
MASTER_FILE = os.path.join(os.path.dirname(__file__), "master.csv")
RECEIPT_DIR = os.path.join(os.path.dirname(__file__), "receipt")
class Item:
    """商品クラス
    """
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price

    def get_price(self):
        return self.price

class Order:
    """オーダークラス
    """
    def __init__(self, item_master):
        self.item_order_list = []
        self.item_master = item_master
        self.sum_price = 0
        self.sum_count = 0
        self.sum_deta = {}

    def add_item_order(self, item_code, item_num):
        for _ in range(item_num):
            self.item_order_list.append(item_code)

    def get_item_data(self, item_code):
        for m in self.item_master:
            if item_code == m.item_code:
                return m.item_name, m.price

    def view_master_list(self):
        for item in self.item_master:
            print("商品コード:{} 商品名:{}     {}円".format(
                item.item_code, item.item_name, item.price))

    def check_order_list(self):
        msg = ""
        for item_order in self.item_order_list:
            if self.sum_deta.get(item_order) is None:
                self.sum_deta[item_order] = 1
            else:
                self.sum_deta[item_order] += 1

        for code, count in self.sum_deta.items():
            name, price = self.get_item_data(code)
            self.sum_price += price*count
            self.sum_count += count
            msg += "商品コード:{} 商品名:{}     {}個".format(code, name, count)
            msg += "\n"
            print("商品コード:{} 商品名:{}     {}個".format(code, name, count))

        # 合計金額、個数の表示
        msg += "\n"
        msg += "合計金額:￥{:,} {}個".format(self.sum_price, self.sum_count)
        msg += "\n"
        print(msg)

    def view_order_list(self):
        msg = ""
        for code, count in self.sum_deta.items():
            name, price = self.get_item_data(code)
            msg += "商品コード:{} 商品名:{}     {}個   {}円".format(code, name, count, count*price)
            msg += "\n"

        # 合計金額、個数の表示
        msg += "\n"
        msg += "合計金額:￥{:,} {}個".format(self.sum_price, self.sum_count)
        msg += "\n"
        print(msg)
        return msg

    def add_order_lst(self):
        item_master_code_list = [x.item_code for x in self.item_master]

        while True:
            input_code = input("商品コードを入力してください。終了の場合は0を入力してください >>> ")
            if input_code in item_master_code_list:
                try:
                    input_num = int(input("個数を入りしてください。 >>> "))
                except ValueError:
                    print("個数は数字で入力してください。")
                    continue
                self.add_item_order(input_code, input_num)
                print("{}をオーダー登録しました".format(input_code))
                self.check_order_list()
            elif input_code == "0":
                break
            else:
                print("コード：{}の商品は登録されていません".format(input_code))

    def check(self):
        while True:
            input_price = int(input("金額を入力>>> "))

            check_price = input_price - self.sum_price

            if check_price > 0:
                print("お釣り:　{}円".format(check_price))
                break
            else:
                print("金額が足りません")

        msg = "お預り金:￥{}\n".format(input_price)
        msg += "お釣り：￥{}".format(check_price)
        return msg


# メイン処理
def main():
    df = pd.read_csv(
        MASTER_FILE,
        dtype={'item_code': str, 'item_name': str, 'price': int}
    )
    item_master_lsit = df.values.tolist()
    item_master = []
    # マスタ登録
    for code, name, price in item_master_lsit:
        item_master.append(Item(code, name, price))

    order = Order(item_master)
    print("オーダー開始")
    order.view_master_list()
    order.add_order_lst()
    print("オーダー終了")
    print("購入開始")
    msg = order.view_order_list()
    msg += order.check()
    file_name =os.path.join(RECEIPT_DIR, "{}.txt".format(datetime.datetime.now().strftime('%Y%m%d%H%M')))
    with open(file_name, mode="a",encoding="utf-8_sig") as f:
        f.write(msg)

    print("購入完了")


if __name__ == "__main__":
    main()
