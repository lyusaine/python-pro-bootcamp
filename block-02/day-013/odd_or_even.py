def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

print("Check if a number is odd or even.")
user_input = int(input("Introduce a number: "))
print(odd_or_even(user_input))