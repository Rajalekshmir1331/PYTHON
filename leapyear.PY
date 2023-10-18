end_year = int(input("Enter the end year: "))
print(f"Leap years from 2023 to {end_year} are:")
for year in range(2023, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
