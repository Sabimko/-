# #1

# # #публичный

# # class Car:
# #     def __init__(self, make, model):
# #         self.make = make
# #         self.model = model #публичный атрибут
        
# #     def display_info(self):
# #         return self.make
# #         return self.model #публичный метод
    
# # print(f'Марка: {self.make}, \n Модель - {self.model}') #вызов к  публичному методу


# #Защищенный
# import datetime

# class Car:
#     def _init_(self, year):
#         self._year = year  # защищенный атрибут _year
        
#     def _calculate_age(self):
#         current = datetime.datetime.now().year
#         return current - self._year

# print(car._year())

# class Car:
#     def __init__(self, mileage):
#         self.__mileage = mileage
        
#     def __update_mileage(self, new_mileage):
#         if new_mileage > self.__mileage:
#             self.__mileage = new_mileage
#         else:
#             print("")
            
#     def set_mileage(self, new_mileage):
#         return self.__update_mileage(new_mileage)
            
    

