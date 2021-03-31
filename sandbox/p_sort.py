def sum_all(numbers):
    return sum(numbers)


num_list = [[2,4,4],[5,5,4,33],[2,1],[10,4],[10,8]]


num_list.sort(key=sum_all)
print(num_list)