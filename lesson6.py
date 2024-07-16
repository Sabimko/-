#Магические методы - dunder методы

# class Work:
#     def __init__(self, position, graphicks):
#         self.position = position
#         self.graphicks = graphicks
        
#     def info(self):
#         print(f"Позиция -{self.position},График-{self.graphicks}")
        
#     def __repr__(self):
#         print(f"Позиция -{self.position},График-{self.graphicks}") 
        
    # def __str__(self):
    #     print(f"Позиция -{self.position},График-{self.graphicks}")  
    
#     def  __call__(self):
#         print("__call__")
        
# work = Work("Бухгалтер",4/2)
# print(work)
# work.info()
# work()

#калькулятор
class  Math:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def __str__(self):
        return f'Первое значение{self.number1}\nВторое значение {self.number2}'
    
    def __add__(self, other):
        """Создать новый обьект как сумму координат 'self' и 'other"""
        print(f'Результат сложение{self.number1} и {self.number2}')
        return Math(self.number1 + other.number1, self.number2)
    
    def __sub__(self, other):
        print(f'Результат вычитание {self.number1} и {self.number2}')
        return Math(self.number1 - other.number1, self.number2)
    
    
    def __mul__(self, other):
        print(f'Результат умножение {self.number1} и {self.number2}')
        return Math(self.number1 * other.number1, self.number2)
    
    
    def __truediv__(self, other):
        print(f'Результат деление {self.number1} и  {self.number2}')
        return Math(self.number1 / other.number1, self.number2)
    

math_number1 = int(input("Введите первое число: "))
math_number2 = int(input("Введите второе  число: "))
math = Math(math_number1,())
math2 = Math(math_number2,())
print(math)
print(math2)

print("Сложение:", math + math2)
print("Вычитание:", math - math2)
print("Умножение:", math * math2)
print("Деление:", math / math2)