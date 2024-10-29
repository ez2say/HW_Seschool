def trace(func):
    def wrapper(*args, **kwargs):
        wrapper.depth += 1
        indent = '    ' * (wrapper.depth - 1)
        print(f"{indent}--> Вход в функцию '{func.__name__}' с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{indent}<-- Выход из функции '{func.__name__}' с результатом {result}")
        wrapper.depth -= 1
        return result
    wrapper.depth = 0
    return wrapper

@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)