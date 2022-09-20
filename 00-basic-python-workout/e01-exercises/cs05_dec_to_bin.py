###
# Converting a base10 num into bin consists in iteratively (integer-dividing) the base10 number
# by 2 until the result is 0.
# The remainders of those operations will give you the bin digits from the least to the most significant
#
# s0:
#   10 // 2 = 5
#   10 %  2 = 0 => 0
# s1:
#   5 // 2 = 2
#   5 %  2 = 1 => 1
# s2:
#   2 // 2 = 1
#   2 %  0 = 0 => 0
# s3:
#   1 // 2 = 0
#   1 %  0 = 1 => 1
# = > 1010

def base10_to_bin(num_str):
    try:
        num = int(num_str)
    except ValueError:
        print("ERROR: a base-10 integer was expected")

    if num < 0:
        print("ERROR: a base-10 positive integer was expected")

    bin_digits = []
    res, rem = (num // 2, num % 2)
    bin_digits.append(str(rem))
    while res > 0:
        res, rem = (res // 2, res % 2)
        bin_digits.append(str(rem))

    bin_digits.reverse()
    print(f"to_bin({num})={''.join(bin_digits)}")


done = False
while not done:
    user_input = input("Enter a base-10 number ('q' to quit): ")
    if user_input.lower() != 'q':
        base10_to_bin(user_input)
    else:
        done = True
