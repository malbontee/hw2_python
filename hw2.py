# 1) Декоратор для проверки аргументов функции: Создайте декоратор, который проверяет типы аргументов функции. Если тип аргумента не соответствует ожидаемому, выбрасывается исключение.

# def type_check(**types):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for name, expected_type in types.items():
#                 if name in kwargs:
#                     value = kwargs[name]
#                 else:
#                     arg_index = list(func.__code__.co_varnames).index(name)
#                     value = args[arg_index]

#                 if not isinstance(value, expected_type):
#                     raise TypeError(f"Error '{name}'")

#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


# @type_check(x=int, y=str)
# def test(x, y):
#     return f"{x} — {y}"

# print(test(5, "hello"))

# /--------------------------------------------------------------------------------------------------/
# 2) Декоратор для кэширования результатов: Напишите декоратор, который будет кэшировать результаты функции. Если функция вызывается с одинаковыми аргументами, то результат должен возвращаться из кэша, а не вызываться заново.

# def cached(func):
#     cache = {}

#     def wrapper(*args):
#         if args in cache:
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result

#     return wrapper


# @cached
# def slow_square(x):
#     return x * x


# print(slow_square(5))
# print(slow_square(5))

# /--------------------------------------------------------------------------------------------------/
# 3) Декоратор для контроля доступа (логин): Напишите декоратор, который проверяет, авторизован ли пользователь. Если нет, выбрасывает исключение. В качестве аргумента функция будет принимать информацию о пользователе.

# def require_login(func):
#     def wrapper(user, *args, **kwargs):
#         if not user.get("is_auth"):
#             raise PermissionError("Не авторизован")
#         return func(user, *args, **kwargs)
#     return wrapper


# @require_login
# def get_profile(user):
#     return f"Профиль: {user['name']}"


# user = {"name": "Влад", "is_auth": True}
# print(get_profile(user))

# /--------------------------------------------------------------------------------------------------/
# 5) Декоратор для повторного выполнения функции при исключении: Создайте декоратор, который повторяет выполнение функции в случае возникновения исключения. Количество попыток и интервал между попытками должны быть переданы как параметры декоратора.

# import time

# def retry(attempts=3, delay=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(attempts):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Ошибка: {e}, попытка {i+1}/{attempts}")
#                     time.sleep(delay)
#             raise Exception("Все попытки исчерпаны")
#         return wrapper
#     return decorator


# @retry(attempts=3, delay=2)
# def unstable():
#     raise ValueError("Error")


# unstable()

# /--------------------------------------------------------------------------------------------------/
# 6) Генератор чисел Фибоначчи: Напишите генератор, который будет возвращать числа Фибоначчи. Генератор должен бесконечно генерировать числа Фибоначчи, пока не будет остановлен.

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# gen = fibonacci()
# for _ in range(10):
#     print(next(gen))

# /--------------------------------------------------------------------------------------------------/
# 7) Генератор чисел, делящихся на 3 или 5: Напишите генератор, который будет генерировать числа, делящиеся на 3 или 5, начиная с 1 и до заданного предела.

# def div_3_or_5(limit):
#     for n in range(1, limit + 1):
#         if n % 3 == 0 or n % 5 == 0:
#             yield n


# print(list(div_3_or_5(30)))

# /--------------------------------------------------------------------------------------------------/
# 8) Напишите генератор, который вычисляет последовательность факториалов для чисел от 1 до бесконечности.

# def factorials():
#     n = 1
#     current = 1
#     while True:
#         current *= n
#         yield current
#         n += 1


# gen = factorials()
# for _ in range(6):
#     print(next(gen)) 

# /--------------------------------------------------------------------------------------------------/
# 9) Напишите генератор, который возвращает только каждый n-й элемент из заданного списка.

# def every_n(lst, n):
#     for i in range(0, len(lst), n):
#         yield lst[i]


# print(list(every_n([1,2,3,4,5,6,7,8], 3)))

# /--------------------------------------------------------------------------------------------------/
# 10) Напишите замыкание, которое позволяет вызвать переданную функцию не более n раз. После превышения лимита должна возвращаться ошибка или сообщение.

# def limit_calls(n):
#     count = 0

#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             if count >= n:
#                 raise Exception("Limit exceeded")
#             count += 1
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


# @limit_calls(3)
# def hello():
#     print("Hello!")


# hello()
# hello()
# hello()
# hello()  

# /--------------------------------------------------------------------------------------------------/
# 11) Создайте замыкание, которое принимает список чисел и возвращает функцию, проверяющую, принадлежит ли число этому списку.

# def in_list(numbers):
#     def checker(x):
#         return x in numbers
#     return checker


# check = in_list([1,2,3,10])
# print(check(10))  
# print(check(5))

# /--------------------------------------------------------------------------------------------------/
# 12) Напишите замыкание, которое принимает шаблон строки и возвращает функцию, которая форматирует строку по этому шаблону.

# def make_formatter(template):
#     def formatter(**kwargs):
#         return template.format(**kwargs)
#     return formatter


# fmt = make_formatter("Привет, {name}! Тебе {age} лет.")
# print(fmt(name="Влад", age=20))

# /--------------------------------------------------------------------------------------------------/
# 13) Создайте замыкание, которое принимает число и возвращает разницу между этим числом и предыдущим вызовом функции.

# def diff_from_prev():
#     prev = None

#     def inner(x):
#         nonlocal prev
#         if prev is None:
#             prev = x
#             return None
#         diff = x - prev
#         prev = x
#         return diff

#     return inner


# f = diff_from_prev()
# print(f(10))  
# print(f(15))  
# print(f(7))   

# /--------------------------------------------------------------------------------------------------/
# 14) Напишите замыкание, которое считает, сколько раз функция была вызвана с каждым уникальным аргументом.

# def count_by_args(func):
#     calls = {}

#     def wrapper(arg):
#         calls[arg] = calls.get(arg, 0) + 1
#         print("Статистика:", calls)
#         return func(arg)

#     return wrapper


# @count_by_args
# def echo(x):
#     return x


# echo(1)
# echo(2)
# echo(1)
