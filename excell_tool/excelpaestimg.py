import os
import os
import glob
import imghdr
import openpyxl
import cv2


# 定数設定
INPUT_IMG_DIR = './tools/INPUT_IMG_DIR/' # 貼り付ける画像を置いておくルートディレクトリ
SHEET_TITLE = '' # シート名の設定
RESULT_FILE_NAME = '.\\result.xlsx' # 結果を保存するファイル名
EX_HIGHT_POINT = 13.5
EX_HIGHT_PX = EX_HIGHT_POINT*1.33
ADJUSRMENT = -4

# ワークブック設定
wb = openpyxl.Workbook()
ws = wb.worksheets[0] # 1番目のシートを編集対象にする
ws.title = SHEET_TITLE # 1番目のシートに名前を設定

# 画像ディレクトリ
dirs = os.listdir(INPUT_IMG_DIR)
cell_num = 1
for dir_name in dirs:
    f_names = INPUT_IMG_DIR + dir_name # ファイル名取得
    size_img = cv2.imread(f_names)
    height, width = size_img.shape[:2]
    img = openpyxl.drawing.image.Image(f_names)
    ws.add_image(img, 'A{}'.format(int(cell_num)))
    cell_num += (height // EX_HIGHT_PX) + ADJUSRMENT # 切り捨て

wb.save(RESULT_FILE_NAME)
