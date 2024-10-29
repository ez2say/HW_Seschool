def validate_range(min_value, max_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, arg_value in enumerate(args):
                if isinstance(arg_value, (int, float)) and not (min_value <= arg_value <= max_value):
                    raise ValueError(
                        f"Аргумент '{func.__code__.co_varnames[i]}' имеет значение {arg_value}, что выходит за пределы [{min_value}, {max_value}]")

            for arg_name, arg_value in kwargs.items():
                if isinstance(arg_value, (int, float)) and not (min_value <= arg_value <= max_value):
                    raise ValueError(
                        f"Аргумент '{arg_name}' имеет значение {arg_value}, что выходит за пределы [{min_value}, {max_value}]")
                
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")


try:
    set_percentage(50)
    set_percentage(150)
except ValueError as e:
    print(e)