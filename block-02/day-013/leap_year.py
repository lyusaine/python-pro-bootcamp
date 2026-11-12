def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print("Check if a year is leap or not.")
user_input = int(input("Introduce a year (yyyy): "))
answer = is_leap(user_input)
if answer:
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is NOT a leap year.")
