# check the algorithm here: https://en.wikipedia.org/wiki/File:Leap_Year_Algorithm.png

def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def read_year_from_input() -> int:
    done = False
    while not done:
        year_str = input("Type the year to check (YYYY): ")
        try:
            year = int(year_str)
            done = True
        except Exception as e:
            print("Incorrect input")
    return year


print("== Leap year checker ==")
year = read_year_from_input()

print(f"The year {year} is a {'leap' if is_leap_year(year) else 'common'} year")
