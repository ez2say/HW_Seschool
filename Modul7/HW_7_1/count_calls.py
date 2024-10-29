def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Функция '{func.__name__}' вызвана {wrapper.calls} раз(а)")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")
greet("Мария")