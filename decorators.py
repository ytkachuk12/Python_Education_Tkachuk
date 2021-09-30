def outside_decorator(var_type):
    """our decorator, take: type of argument what we want to check"""
    def type_check(func):
        """checker, take function like argument"""
        def wrapper(func_var):
            """wrapper, take argument of decoration function"""
            if isinstance(func_var, var_type):
                return func(func_var)
            else:
                raise TypeError
        return wrapper
    return type_check


@outside_decorator(float)
def some_func(num):
    return num ** 2


@outside_decorator(str)
def another_funk(string):
    return string + "!!!"


print(some_func(6.252))
print(another_funk(6))
