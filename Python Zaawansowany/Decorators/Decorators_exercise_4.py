def arg_check(specified_type):
    def check(func):
        def inner(func_arg):
            if not isinstance(func_arg, specified_type):
                raise TypeError(f"Function argument does not "
                                f"match specified type: {specified_type}")
            check(func(func_arg))
        return inner
    return check


@arg_check(float)
def test_func(variable):
    return print(variable)
