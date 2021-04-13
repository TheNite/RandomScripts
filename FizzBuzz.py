def fizz_buzz(numb):
    if numb % 15 == 0:
        return "FizzBuzz"
    elif numb % 5 == 0:
        return "Buzz"
    elif numb % 3 == 0:
        return "Fizz"
    else:
        return numb


def fizzBuzz(numb):
    if numb % 3 == 0 and numb % 5 == 0:
        return "FizzBuzz"
    elif numb % 5 == 0:
        return "Buzz"
    elif numb % 3 == 0:
        return "Fizz"
    else:
        return numb


for number in range(1, 31):
    print(f"1: {fizz_buzz(number)}, 2: {fizzBuzz(number)}")
