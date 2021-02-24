from blueqat import Circuit

# 量子の重ね合わせ
# 0と1の重ね合わせによって測定するたびに答えが50％ずつに
Circuit().h[0].m[:].run(shots=100)

# 量子もつれ
# 重ね合わせからデータを絞り込む
Circuit().h[0].cx[0, 1].m[:].run(shots=100)

Circuit().h[0].h[1].m[:].run(shots=100)