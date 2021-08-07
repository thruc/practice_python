import os

# キャラクターリストのファイル
SRC_FILE = os.path.join(os.path.dirname(__file__), "source.csv")

def search():
    """検索ツール
    """
    with open(SRC_FILE, encoding="utf-8") as f:
        chara_list = f.read().split(",")

    # 検索ワード
    search_word = input("鬼滅の登場人物の名前を入力してください >>> ")

    # 検索
    if search_word in chara_list:
        # 入力したキーワードがキャラクターリストに存在している場合
        print(f"{search_word}が見つかりました")
    else:
        # 入力したキーワードがキャラクターリストに存在しない場合
        print(f"{search_word}が見つかりません")
        # キャラクターリストに追加
        chara_list.append(search_word)
        # キャラクターリストをファイルに上書き
        with open(SRC_FILE, mode='w', encoding="utf-8") as f:
            f.write(','.join(chara_list))

if __name__ == "__main__":
    search()
