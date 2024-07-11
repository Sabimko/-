# #Инкапсуляция

# #публичный
# class PublicExample:
#     def __init__(self, value):
#         self.value = value #публичный атрибут
        
#     def info(self):
#         return self.value #публичный метод
    
# public = PublicExample(42)

# print(public.info()) #вызов публичный метод
# print(public.value()) #доступ к публичному атрибуту

# #защищенный

# class ProtectedExample:
#     def __init__(self, value):
#         self._value = value #защищенный атрибут
        
#     def _info(self):
#         return self._value #защищенный метод
    
# protected = ProtectedExample(43)
# print(protected._value) #Вызов защищенный метод
# print(protected._info()) #Доступ к защищенному атрибуту


#Приватный

class PrivateExample:
    def __init__(self, value):
        self.__value = value #Приватный атрибут
        
    def __info(self):
        return self.__value #Приватный метод
    
    def acces_private(self):
        return self.__info() #публичный метод,где мы получаем доступ к приватному атрибуту
    
private = PrivateExample(55)
#Прямой доступ к приватному атрибуту вызовкт ошибку
# print(private.__value)

#Прямой доступ к приватному методу вызовкт ошибку
# print(private.__info())

#Доступ через публичный метод
# print(private.acces_private())

#Доступ к приватному атрибуту через имя mangling
# print(private._PrivateExample__value)


#1
# class Example(PrivateExample):
#     pass

# print(private.acces_private())
# print(private._PrivateExample__value)


# #2
# class Example(PrivateExample):
#     def __init__(self, value, current):
#         super().__init__(value)
#         self._current = current
        
#     def public(self):
#         print(f'Приватный - {self.acces_private()}, Защищенный - {self._current}')
    
# example = Example(3, 5)
# print(example.public())

# # print(private.acces_private())
# # print(private._PrivateExample__value)

