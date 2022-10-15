from random import randint

consecutive_even_nums_count = 0
while True:
    num = randint(1, 6)
    print(f"Num obtained: {num}")
    if (num % 2 == 0):
        consecutive_even_nums_count += 1
        print(f"{consecutive_even_nums_count} consecutive even nums!")
    else:
        print(f"Exiting because {num} is an odd number")
        quit()
