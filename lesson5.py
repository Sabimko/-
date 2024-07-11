#Практика
# #1
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
        
#     def display_info(self):
#         print(f'Марка:{self.brand}\nМодель:{self.model}\nГод выпуска:{self.year}')
        
# car = Car("BMW","BMW X6 M",2010)
# # print(car.display_info())


# #2
# class ElectricCar(Car):
#     def __init__(self, brand, model, year, capacity=2000):
#         super().__init__(brand, model, year)
#         self._capacity = capacity
        
#     def display_battery_info(self):
#         print(f'Марка:{self.brand}\nМодель:{self.model}\nГод выпуска:{self.year}/nЕмкость батареи:{self._capacity}kWh')

# car = Car("BMW","BMW X6 M",2010,2000)        
# print(Car.display_info())

# #3
class Car:
        def __init__(self, brand, model, year, mileage):
            self.brand = brand
            self.model = model
            self.year = year
            self.__mileage = mileage
            
        def display_info(self):
        print(f'Марка:{self.brand}\nМодель:{self.model}\nГод выпуска:{self.year}')
        
    def set_mileage(self):
        return(f"Ec:{self.__mileage}")
    def get_mileage(self):
        return(f've:{self.set_mileage}')
    
    
class Dog:
    def make_sound(self):
        print("woof")
        
class Cat:
    def make_sound(self):
        print("meow")
        
animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound(b)