def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Неверный тип аргумента '{arg}'. Ожидался {expected_type}, получен {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

try:
    print(add(2, 3))
    print(add(2, '3'))
except TypeError as e:
    print(e)