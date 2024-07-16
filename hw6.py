
# #1

# class MagicCalculator:
#     def __init__(self, number_1, number_2):
#         self.number_1 = number_1
#         self.number_2 = number_2

#     def __add__(self, other):
#         return MagicCalculator(self.number_1 + other.number_1, self.number_2 + other.number_2)

#     def __sub__(self, other):
#         return MagicCalculator(self.number_1 - other.number_1, self.number_2 - other.number_2)

#     def __mul__(self, other):
#         return MagicCalculator(self.number_1 * other.number_1, self.number_2 * other.number_2)

#     def __truediv__(self, other):
#         return MagicCalculator(self.number_1 / other.number_1, self.number_2 / other.number_2)

#     def __floordiv__(self, other):
#         return MagicCalculator(self.number_1 // other.number_1, self.number_2 // other.number_2)

#     def __repr__(self):
#         return f"MagicCalculator(number_1={self.number_1}, number_2={self.number_2})"


# calc1 = MagicCalculator(10, 20)
# calc2 = MagicCalculator(2, 4)

# print(calc1 + calc2)  
# print(calc1 - calc2)  
# print(calc1 * calc2)  
# print(calc1 / calc2)  
# print(calc1 // calc2)  



# #2

# class Book:
#     def __init__(self, title, author, year, genre=None):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre = genre

#     def __lt__(self, other):
#         return self.year < other.year

#     def __le__(self, other):
#         return self.year <= other.year

#     def __gt__(self, other):
#         return self.year > other.year

#     def __ge__(self, other):
#         return self.year >= other.year

#     def __eq__(self, other):
#         return self.year == other.year

#     def __ne__(self, other):
#         return self.year != other.year

#     def __str__(self):
#         return f"'{self.title}' by {self.author}, {self.year} ({self.genre})" if self.genre else f"'{self.title}' by {self.author}, {self.year}"


# book1 = Book("Дилимдеги", "Алимырза Назаров", 2024, "Кундолук дептер")
# book2 = Book("Бир гана сенсин", "Нуржигит Кадырбеков", 2018, "Проза")
# book3 = Book("Каректен аккан коз жаш", "Рустам Абилов", 2021, "Баян")

# print(book1)  
# print(book2)  

# print(book1 > book2) 
# print(book1 == book3)  
# print(book2 < book3)  
