# Leap Year finding
year = int(input("Which year do you want to check"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"So the year {year} is a Leap year")
        else:
            print(f"So the year {year} is not a Leap year")
    else:
        print(f"So the year {year} is a Leap year")
else:
    print(f"So the year {year} is not a Leap year")
