# dict

マージ（|）および更新（| =）演算子

別の辞書に含まれる要素の中で、キーが対象の辞書の中に同じものがあった場合、対象の辞書のキーに対する値が別の辞書の方の値で更新されます。また別の辞書に含まれる要素の中で、対象の辞書の中に同じキーが存在しなかった場合、対象の辞書に新しい要素として追加されます。

```python
>>> x = {"key1": "value1 from x", "key2": "value2 from x"}
>>> y = {"key2": "value2 from y", "key3": "value3 from y"}
>>> x | y
{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
>>> y | x
{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}
```

# str.removeprefix(prefix) 
New String Methods to Remove Prefixes and Suffixes

# 型ヒント
コンテナ系は、内包する型を指定するので、 list[str] などと表記を行いたい。しかし、これはPythonの文法エラーとなってしまいその為に、typingでは大文字の型 (例えば List, Tuple, Dict, Set) を準備していが
対応するをtypingからインポートする代わりに、 list や dict のような組み込みのコレクション型を汎用型として使うことができるようになりました。標準ライブラリ内の他のいくつかの型も汎用型になりました。


```python
def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)
```

# new-parser
parserがLL（１）法からLR法になった
https://docs.python.org/3/whatsnew/3.9.html#new-parser

https://ja.wikipedia.org/wiki/LL%E6%B3%95

https://ja.wikipedia.org/wiki/LR%E6%B3%95

# その他変更
- インポート時のエラーがValueErrorではなくImportErrorをあげるようになる

- ローカルファイルを実行した時の実行時のパスが絶対パスになる
python script.pyとした時に__file__属性にその実行したスクリプトのファイル名が入りますが、これまではコマンドラインで書かれたままの相対パスでしたが、3.9からは絶対パスになります。

それから、過去の議論を追うと、 sys.argv[0]も絶対パスに変えちゃおうとしていたみたいです。が、そこは影響範囲が大きすぎるといういうツッコミが入り、そちらは取りやめになったみたいです。確かにそれはちょっとやり過ぎだと思うので良かったです。

- Pythonの開発モードとデバッグビルドでは、 エンコードおよびエラーの引数は、現在の文字列のエンコードとデコードの操作のためにチェックされます。open()、str.encode() bytes.decode()


```python

>>> 'b'.encode('cp932').decode('utf-8', errors='Boom, Shaka Laka, Boom!')
'b'
>>>

```

```python

>>> 'b'.encode('cp932').decode('utf-8', errors='Boom, Shaka Laka, Boom!')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: unknown error handler name 'Boom, Shaka Laka, Boom!'
>>>

```


- 空文字列("")に対するreplaceの挙動の変更
空文字列("")に対して replaceメソッドを適用した時の挙動が変わります。これまでは、オプションのcount引数（最大何回変更を適用するかを指定する）が付いているとおかしな結果が出ていました。

```
"".replace("", "p") = "p"
"".replace("", "p", 1) = ""
"".replace("", "p", 2) = ""
```
これが、3.9になると
```
"".replace("", "p") = "p"
"".replace("", "p", 1) = "p"
"".replace("", "p", 2) = "p"
```

- デコレーターに関する制約の緩和
「decorator」の定義がPython 3.8では「"@" dotted_name ["(" [argument_list [","]] ")"] NEWLINE」となっているのが、Python 3.9では「"@" assignment_expression NEWLINE」と変更

Python 3.9では
```python
>>> def make_decorators():
...     def decorator0(func):      
...         def inner_func0(*args):
...             print('decorator 0')
...             return func(*args)
...         return inner_func0
...     def decorator1(func):
...         def inner_func1(*args):
...             print('decorator 1')
...             return func(*args)
...         return inner_func1
...     return [decorator0, decorator1]
...
>>> decorators = make_decorators()
>>>
>>> @decorators[0]
... def hello():
...     print('hello')
...
>>> @decorators[1]
... def goodbye():
...     print('goodbye')
...
>>> hello()
decorator 0
hello
>>> goodbye()
decorator 1
goodbye
>>>
```
Python 3.8ではエラーとなる
```python
>>> def make_decorators():
...     def decorator0(func):
...         def inner_func0(*args):
...             print('decorator 0')
...             return func(*args)
...         return inner_func0
...     def decorator1(func):
...         def inner_func1(*args):
...             print('decorator 1')
...             return func(*args)
...         return inner_func1
...     return [decorator0, decorator1]
...
>>> decorators = make_decorators()
>>>
>>> @decorators[0]
  File "<stdin>", line 1
    @decorators[0]
               ^
SyntaxError: invalid syntax
>>> def hello():
...     print('hello')
...
>>> @decorators[1]
  File "<stdin>", line 1
    @decorators[1]
               ^
SyntaxError: invalid syntax
>>> def goodbye():
...     print('goodbye')
...
```


Python 3.8での回避法
```python
>>> # リストからデコレーターを取り出して、デコレーターにインデックス指定が
>>> # 含まれないようにする
>>> decorator0 = decorators[0]
>>> decorator1 = decorators[1]
>>>
>>> @decorator0
... def hello():
...     print('Hello')
...
>>> @decorator1
... def goodbye():
...     print('Goodbye')
...
>>> hello()
decorator 0
Hello
>>> goodbye()
decorator 1
Goodbye
>>>
>>> # 引数をそのまま返す関数を定義し、インデックス指定は、
>>> # 関数の引数に含めるようにする。_x自体はdotted_nameなので問題ない
>>> def _x(func):
...     return func
...
>>> @_x(decorators[0])
... def hello():
...     print('hello')
...
>>> @_x(decorators[1])
... def goodbye():
...     print('goodbye')
...
>>> hello()
decorator 0
hello
>>> goodbye()
decorator 1
goodbye
>>>
```



# 新規追加モジュール

## zoneinfo

# 改良モジュール

## ast

3.9：インデントオプションが追加されました
whatsnew39\ast_prac.py