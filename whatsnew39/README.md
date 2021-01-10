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