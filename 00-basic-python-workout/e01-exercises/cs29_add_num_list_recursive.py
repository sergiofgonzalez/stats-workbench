
def sum_list(nums):
    def do_sum(idx=0):
        if idx == len(nums) - 1:
            return nums[idx]
        else:
            return nums[idx] + do_sum(idx + 1)

    return do_sum()


print(f"{sum_list((1, 2, 3))=}")
print(f"{sum_list((1, 2, 4, 8, 16, 32, 64))=}")
