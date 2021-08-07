
# exeファイル
格納場所
/dist/create_table.exe

実行方法
入力ファイルをcreate_table.exeファイルにドラッグ＆ドロップ
出力ファイルは`output.xslx`



# pythonコード
格納場所
本体は`create_table.py`に格納

実行方法

仮想環境を有効にする

```
.venv/Scripts/activate.bat

```

第一引数に入力ファイルのパスを渡して実行

```
python create_table.py ./input.xlsx
```

# 修正後exeファイル生成

仮想環境を有効化

```
.venv/Scripts/activate.bat
```

exeファイルの生成
```
pyinstaller create_table.py --name create_table --onefile
```