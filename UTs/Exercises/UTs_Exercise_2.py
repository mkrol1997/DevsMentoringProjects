def fizz_buzz(number: int) -> str:
    if isinstance(number, int):
        if number > 2:
            if number % 3 == 0 and number % 5 == 0:
                return "FizzBuzz"
            elif number % 3 == 0:
                return "Fizz"
            elif number % 5 == 0:
                return "Buzz"
            else:
                return "Wrong number"
        else:
            raise Exception("Number must be an integer greater than 1")
    else:
        raise TypeError("Wrong type: expected class <int>")