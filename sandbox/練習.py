
def 泡(数字: list[int]) -> list[int]:
    数字配列の長さ = len(数字)
    for い in range(数字配列の長さ):
        for ろ in range(数字配列の長さ - 1 - い):
            if 数字[ろ] > 数字[ろ + 1]:
                数字[ろ], 数字[ろ + 1] = 数字[ろ + 1], 数字[ろ]

    return 数字


if __name__ == '__main__':
    import random
    数字 = [random.randint(0, 1000) for い in range(10)]
    print(数字)
    print(泡(数字))