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
https://docs.python.org/3/whatsnew/3.9.html#new-parser