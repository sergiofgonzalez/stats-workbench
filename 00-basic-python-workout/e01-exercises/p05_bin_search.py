# we need to keep track of start, end, middle
# do not create a new list with sliced list as this will ruin the found index




def find_val_in_list(sorted_list, target_value):
    middle = 0
    start = 0
    end = len(sorted_list) # when slicing, the 2nd index is non-inclusive
    steps = 0

    while start < end:
        # print(f"\n   >> s{steps}")
        steps = steps + 1

        middle = start + (end - start - 1) // 2
        # print(f"   >> list: {sorted_list[start:end]}, middle={middle}")

        # print(f"   >> Comparing target {target_value} <=> s[{middle}]={sorted_list[middle]}")
        if target_value == sorted_list[middle]:
            return middle
        elif target_value < sorted_list[middle]:
            end = middle
        else:
            start = middle + 1

    return -1 # not found

# searching for 8
# s0
# index:      0  1  2  3  4  5  6  7  8
# list:     [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], start=0, end=9, middle=(9-1)//2=4
#                         X
#
#           8 > 5 => start = 5

# s1
# index:      0  1  2  3  4  5  6  7  8
# list:                    [ 6, 7, 8, 9 ] start=5, end=9, middle=5 + (9-5-1)//2=6
#                               X
#
#           8 > 7 => start = 7

# s2
# index:      0  1  2  3  4  5  6  7  8
# list:                          [ 8, 9 ] start=7, end=9, middle=7 + (9-7-1)//2=7
#                                  X
#
#           8 == 8 => found


# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)}")
# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)}")
# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)}")

# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 8) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 8)}")
# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)}")
# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)}")

# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)}")
# print(f"find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) = {find_val_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)}")

num_list = list(range(1, 21))
for i in range(1, 21):
    print(f"find_val_in_list({num_list}, {i}) = {find_val_in_list(num_list, i)}")