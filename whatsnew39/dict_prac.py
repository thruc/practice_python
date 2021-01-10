x1 = {"one":"A", "two":"B", "three":"C"}
y1 = {"two":"b", "four":"d"}
x1.update(y1)


x2 = {"one":"A", "two":"B", "three":"C"}
y2 = {"two":"b", "four":"d"}
x2 ={**x2, **y2}


x3 = {"one":"A", "two":"B", "three":"C"}
y3 = {"two":"b", "four":"d"}
# 3.9からマージ（|）および更新（| =）演算子が組み込みのdictクラスに追加されました。
# これらは、辞書をマージする既存のdict.updateおよび{** d1、** d2}メソッドを補完します。
x3 |= y3
print(x1==x2==x3)

