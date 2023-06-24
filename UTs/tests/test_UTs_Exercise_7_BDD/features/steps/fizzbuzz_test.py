from behave import Given, When, Then
from UTs.Exercises.UTs_Exercise_2 import fizz_buzz


@Given('Number divisible by 3 and 5')
def step_impl(context):
    pass


@Given('Number divisible by {divisor} and not by {not_a_divisor}')
def step_impl(context, divisor, not_a_divisor):
    pass


@Given('Integer number from positive range')
def step_impl(context):
    pass


@When('I FizzBuzz the number {number}')
def step_impl(context, number):
    context.result = fizz_buzz(int(number))


@Then('I should get {result}')
def step_impl(context, result: str):
    assert context.result == result


@Given('String passed as function argument')
def step_impl(context):
    pass


@When('I try to FizzBuzz the string {number}')
def step_impl(context, number: int):
    try:
        fizz_buzz(number)
    except TypeError as err:
        context.exc = err


@Given('Number is from negative range')
def step_impl(context):
    pass


@When('I try FizzBuzz the negative number {number}')
def step_impl(context, number):
    try:
        fizz_buzz(int(number))
    except Exception as err:
        context.exc = err


@Then('It raises {error_type} with message {msg}')
def step_impl(context, error_type, msg):
    assert type(context.exc) == eval(error_type)
    assert str(context.exc) == msg
