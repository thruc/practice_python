ages_descending = [1,22,33,4,6,3,8,9,4,5,6,77,8,45]
ages_descending.sort(reverse=True)

oldest, second_oldest, *others = ages_descending
print(oldest, second_oldest, others)