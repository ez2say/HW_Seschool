def call_limit(max_calls):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            if wrapper.calls > max_calls:
                raise RuntimeError(f"Превышено максимальное количество вызовов функции '{func.__name__}'")
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator

@call_limit(max_calls=3)
def print_message(msg):
    print(msg)

print_message("Первый вызов")
print_message("Второй вызов")
print_message("Третий вызов")
print_message("Четвертый вызов")