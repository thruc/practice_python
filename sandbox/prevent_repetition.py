fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

# countに代入をしながら判定
if (count := fresh_fruit.get('apple', 0)) >= 4:
    print("make_cider_{}".format(count))
else:
    print("out_of_stock")