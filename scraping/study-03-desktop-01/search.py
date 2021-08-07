import pandas as pd
import eel

# デスクトップアプリ作成課題


def kimetsu_search(word, csv):
    # 検索対象取得
    df = pd.read_csv(csv)
    source = list(df["name"])

    # 検索
    if word in source:
        msg = "『{}』はあります".format(word)
        print(msg)
        eel.view_log_js(msg + "\n")
    else:
        msg = "『{}』はありません".format(word)
        print(msg)
        eel.view_log_js(msg + "\n")
        source.append(word)

    # CSV書き込み
    df = pd.DataFrame(source, columns=["name"])
    df.to_csv(csv, encoding="utf_8-sig")
    print(source)
