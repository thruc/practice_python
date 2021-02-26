# ElliotWaveAnalysis
Elliot Wave Analyzer for OHLC data

## 準備

### 仮想環境構築
既に仮想環境構築されている場合は省略
```
python -m venv venv
```

### 仮想環境起動
windows
```
\ElliotWaveAnalysis>venv\Scripts\activate.bat
```
mac
```
\ElliotWaveAnalysis>source venv\Scripts\activate
```

### モジュールインストール
既にインストールされている場合は省略
```
pip install -r requirements.txt
```

### Pair_Analysis.txtに記載されているディレクトリを作成

「XXX_YY」の記載があれば
「./ForexData/XXX/XXX_YY.csv」にOHLCのデータのファイルを置く

例：USDJPY_DがPair_Analysis.txtに記載されている場合
「./ForexData/USDJPY/USDJPY_D.csv」にOHLCのデータのファイルを置く

## 実行

```
\ElliotWaveAnalysis>python Handler.py
```

### その他
Handler.pyで使用していない関数があったため
export_OHLC_graph.ipynbで実行の仕方を記載





