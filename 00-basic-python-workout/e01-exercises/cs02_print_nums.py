# Read nums from the console until a zero is entered,
# then print them in the order they were entered and
# in the reversed order

nums = []
nums_reversed = []

done = False
while not done:
    num_str = input("Enter a integer number (0 to end): ")
    if num_str == '0':
        done = True
    else:
        num = int(num_str)
        if not isinstance(num, int):
            print(f'ERROR: only integers are allowed and you typed {num_str}!')
        else:
            nums.append(num)
            nums_reversed.insert(0, num)

print("You've entered:")
print(nums)
print(nums_reversed)

print("\nAlso:")
nums.reverse()
print(nums)
