import  requests
import time

"""
Декораторы - это функции, которые позволяют или расширять поведение других функций

@simple_decorator
def hello():
    pass
"""
# def simple_decorator(func):
#     def wrapper():
#         print("Перед вызовом функции")
#         func()
#         print("После вызова функции")
#     return wrapper
#
# @simple_decorator
# def hello():
#     print("hello!")
#
# hello()

def timing(func):
    def wrapper(*args, **kwargs):
        stat_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {end_time - stat_time:.4f} секунд")
    return wrapper

@timing

def google_request(url, name):
    response = requests.get(url)
    print(response.status_code)
    print(name)

url = "https://google.com"
google_request(url, name='Alena')