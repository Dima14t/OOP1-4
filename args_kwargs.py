def hello(name1, name2, name3):
    print("hello", name1)
    print("hello", name2)
    print("hello", name3)

# hello("Alena", "Masha", "Sasha")
#
#  * - оператор распоковки
#
# def hi(*args):
#     for name in args:
#       print(f"Hello, {name}")
#
# hi("Alena", "Masha", "Sasha")

def car_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")

car_info(brand="BMW")
car_info(brand="BMW", model="x5")
car_info(brand="BMW", model="x5", color="Black")

def person_info(*args, **kwargs):
    print(args)
    print(kwargs)

person_info("Ivan", "Petrov", gender="male", phone="23345345")
# "Ivan", "Petrov" - *
# gender="male", phone="23345345" - **