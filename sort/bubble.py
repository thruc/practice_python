
def bubble_sort(nums: list[int]) -> list[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(nums)
    print(bubble_sort(nums))
