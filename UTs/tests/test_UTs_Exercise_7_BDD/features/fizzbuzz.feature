Feature: Fizzbuzz function test
  Scenario: Integer number from positive range
    Given Number divisible by 3 and 5
    When I FizzBuzz the number 15
    Then I should get FizzBuzz

  Scenario: Integer number from positive range
    Given Number divisible by 5 and not by 3
    When I FizzBuzz the number 5
    Then I should get Buzz

  Scenario: Integer number from positive range
    Given Number divisible by 3 and not by 5
    When I FizzBuzz the number 3
    Then I should get Fizz

  Scenario: Integer number from positive range
    Given Integer number from positive range
    When I FizzBuzz the number 16
    Then I should get Wrong number

  Scenario: Function argument not an integer
    Given String passed as function argument
    When I try to FizzBuzz the string test_string
    Then It raises TypeError with message Wrong type: expected class <int>

  Scenario: Integer number from negative range
    Given Number is from negative range
    When I try FizzBuzz the negative number -15
    Then It raises Exception with message Number must be an integer greater than 1