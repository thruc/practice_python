from typing import List

# typingで大文字の型を使用
def greet_all_38(names: List[str]) -> None:
    for name in names:
        print("Hello", name)

# 組み込みのコレクションをそのまま使用できる
def greet_all_39(names: list[str]) -> None:
    for name in names:
        print("Hello", name)


names = ["Hoge","Fuga"]

greet_all_38(names)
greet_all_39(names)