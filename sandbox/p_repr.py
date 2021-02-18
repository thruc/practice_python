import datetime
today = datetime.date.today()
str(today)
repr(today)  # objectを文字列representation
x = eval(repr(today))  # 文字列をobject文字列をPythonの式として実行する関数evaluate
print(x)
