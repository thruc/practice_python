import pandas as pd
# 定数設定
SHEET_TITLE = '自己クロス表' # シート名の設定
OUTPUT_FILE = './output.xlsx' # 出力力ファイル名


def create_cross_table(input_path:str):
    """自己クロス表作製

    Args:
        input_path (str): 元データのエクセルのファイルパス
    """
    df = pd.read_excel(input_path, engine='openpyxl')
    df = pd.get_dummies(df,prefix="",prefix_sep="")
    df = df.groupby('社員番号')
    df = df.sum()
    sum_lsit=[]
    for name, time in df.iteritems():
        df_sum = df[df[name]>0].sum()
        df_sum.name = name
        sum_lsit.append(df_sum)
    df_result = pd.concat(sum_lsit, axis=1)
    df_result.T.to_excel(OUTPUT_FILE, sheet_name=SHEET_TITLE, engine='openpyxl')


if __name__ == "__main__":
    import sys

    path = sys.argv[1]
    create_cross_table(path)