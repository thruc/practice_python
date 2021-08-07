

def partition(nums: list[int], low: int, high: int) -> int:
    i = low - 1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1


def quick_sort(nums: list[int]) -> list[int]:
    def _quick_sort(nums: list[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(nums, low, high)
            _quick_sort(nums, low, partition_index-1)
            _quick_sort(nums, partition_index+1, high)

    _quick_sort(nums, 0, len(nums)-1)
    return nums


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(quick_sort(nums))
