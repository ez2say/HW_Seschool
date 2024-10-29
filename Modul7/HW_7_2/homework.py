from functools import reduce
from math import factorial

#Задача №1#

str_arr = ["1", "20", "300"]
numbers = list(map(int, str_arr))
print(numbers)

#Задача №2#

num_array = [1, 2, 3, 4, 5, 6]
filtered_array = list(filter(lambda x: x % 2 == 0, num_array))
print(filtered_array)

#Задача №3#

start_nums = [1, 2, 3, 4]
finish_nums = list(map(lambda x: x ** 2, start_nums))
print(finish_nums)

#Задача №4#

text_array = ["cat", "elephant", "dog", "tiger"]
new_text_array = list(filter(lambda x: len(x) > 3, text_array))
print(new_text_array)

#Задача №5#

array = [1, 2, 3, 4]
num = reduce(lambda x, y: x * y, array)
print(num)

#Задача №6#

str_array = ["hello", "world", "Python"]
new_array = list(map(len, str_array))
print(new_array)

#Задача №7#

list_fruit = ["apple", "banana", "pear", "strawberry"]
longest = reduce(lambda x, y: x if x > y else y, map(len, list_fruit))
print(longest)

#Задача №8#

words = ["hello", "world"]
upper_words = list(map(str.upper, words))
print(upper_words)

#Задача №9#

numbers_str = ["1", "2", "3", "4"]
numbers_int = map(int, numbers_str)
squared_even_numbers = list(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers_int)))
print(squared_even_numbers)

#Задача №10#

numbers = [-2, 3, -4, 5, 6]
positive_numbers = filter(lambda x: x > 0, numbers)
product = reduce(lambda x, y: x * y, positive_numbers, 1)
print(product)

#Задача №11#

words = ["apple", "banana", "orange", "grape"]
vowel_words = filter(lambda x: x[0].lower() in 'aeiou', words)
lengths = list(map(len, vowel_words))
print(lengths)

#Задача №12#

words = ["racecar", "hello", "level", "world"]
reversed_words = map(lambda x: x[::-1], words)
palindromes = list(filter(lambda x: x == x[::-1], reversed_words))
print(palindromes)

#Задача №13#

numbers = [2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
factorials = map(factorial, even_numbers)
product = reduce(lambda x, y: x * y, factorials, 1)
print(product)

#Задача №14#

words = ["hello", "world", "Python", "is", "great"]
even_length_words = filter(lambda x: len(x) % 2 == 0, words)
upper_words = map(str.upper, even_length_words)
result = ' '.join(upper_words)
print(result)

