import eel
import pandas as pd

import desktop
import pos_sys

app_name = "html"
end_point = "index.html"
size = (600, 900)

df = pd.read_csv(
    pos_sys.MASTER_FILE,
    dtype={'item_code': str, 'item_name': str, 'price': int}
)
item_master_lsit = df.values.tolist()
item_master = []
# マスタ登録
for code, name, price in item_master_lsit:
    item_master.append(pos_sys.Item(code, name, price))

order = pos_sys.Order(item_master)

@ eel.expose
def view_menu():
    # メニューを画面に出力する
    eel.view_menu_js(order.view_menu())


@ eel.expose
def crate_select():
    eel.view_select_js(order.create_select())

@ eel.expose
def add_order(code, order_num):
    # オーダー登録
    order.add_item_order(code, int(order_num))
    print("オーダー登録")

    # オーダー内容を画面に表示する
    confirm = order.check_order_list()
    eel.view_confirm_js(confirm)


@ eel.expose
def check(recieved):
    # おつりを計算して画面に表示する
    order.recieved = int(recieved)
    msg, flg = order.culc_change()
    eel.view_change_js(msg)
    if flg:
        order.export_receipt()

desktop.start(app_name, end_point, size)
