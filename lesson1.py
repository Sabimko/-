# OOП - обьектно- ориентированние програмирование

# class Person:
#     def __init__(self, name, lastname,age, nayionalety):
#         #__init__---конструктор
#         #self, name, lastname,age, nayionalety ---обьект конструктора
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.nayionalety = nayionalety
        
#     def info(self):
#         print(f"Имя{self.name}, Фамилия {self.lastname}, Вoзраст{self.age},Нация{self.nayionalety} ")
# Person = Person("Сабира","Тологон кызы", 21, "Кыргыз")
# Person.info()

# class Car: 
#     def __init__(self, model, year, color, volume):
#         self.model = model
#         self.year = year
#         self.color = color 
#         self.volume = volume
    
#     def info(self):
#         print(f"Модель машины: {self.model}, Год выпуска: {self.year}, Цвет: {self.color}, Объем: {self.volume}")
        
# bmw = Car('BMW', 2016, 'black', '2.5')
# lexus = Car('Lexus', '2023', 'White', '4')
# bmw.info()
# lexus.info()

# class calculator:
##1
#     def sum(self, x, y):
#         return x + y
    
#     def subtraction(self, x,y):
#         return x - y
    
#     def multiplication(self , x, y):
#         return x * y
    
#     def division (self, x,y):
#         if y == 0:
#             print("Ошибка!")
#         else:
#             return x / y
        
# cals = calculator()    

# print("1 + 5=",cals.sum(1,5))
# print("10 - 5=",cals.subtraction(10,5))
# print("7 * 5",cals.multiplication(7,5))
# print("100 / 5",cals.division(100,5))


##2
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
      
#     def plus(self):
#         print(f'Ответ: {self.num1 + self.num2}')
        
#     def minus(self):
#         print(f'Ответ: {self.num1 - self.num2}')
        
# calc = Calculator(2, 2)
# calc.plus()
# calc.minus()

##3
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def plus(self):
#         print(f'Ответ: {self.num1 + self.num2}')
        
#     def minus(self):
#         print(f'Ответ: {self.num1 - self.num2}')
        
#     def multiplication(self):
#         print(f'Ответ: {self.num1 * self.num2}')
        
#     def division(self):
#         print(f'Ответ: {self.num1 / self.num2}')
        
# num1 = float(input("Введите первое число: "))
# operator = input("+, -, *, /: ")
# num2 = float(input("Введите вторе число: "))

# calc = Calculator(num1, num2)

# if operator == '+':
#     calc.plus()
# elif operator == '-':
#     calc.minus()
# elif operator == '*':
#     calc.multiplication()
# elif operator == '/':
#     calc.division()
# else:
#     print("Неверный оператор")

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
        
#     def info(self):
#         print(f"Книга:{self.title}\nАвтор:{self.author} ")
        
# book = Book("Звезды","Тологон кызы")
# book.info()
            