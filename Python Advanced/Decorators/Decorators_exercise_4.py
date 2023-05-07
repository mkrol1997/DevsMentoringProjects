from typing import Any


def arg_check(specified_type: Any):
    """ Checks if decorated function argument is of
      the same type as type specified in decorator argument """
    def check(func):
        def inner(func_arg: Any) -> check:
            if not isinstance(func_arg, specified_type):
                raise TypeError(f"Function argument does not "
                                f"match specified type: {specified_type}")
            return check(func(func_arg))
        return inner
    return check


@arg_check(float)
def test_func(variable: Any) -> None:
    print(variable)
