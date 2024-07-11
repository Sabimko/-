class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self):
        add = self.__cpu + self.__memory
        sub = self.__cpu - self.__memory
        multiply = self.__cpu * self.__memory
        if self.__memory != 0:
            div = self.__cpu / self.__memory
        else:
            div = "неопределено (деление на ноль)"
        return f"Результаты: Сложение: {add}, Вычитание: {sub}, Умножение: {multiply}, Деление: {div}"

    def getteri_cpu(self):
        return self.__cpu

    def getteri_memory(self):
        return self.__memory

    def info(self):
        return f"Компьютер с процессором:{self.__cpu} и памяту {self.__memory}. {self.__make_computations()}"

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        return f"Ноутбук с процессором: {self.getteri_cpu()}, Памятью: {self.getteri_memory()}, и картой памяти: {self.__memory_card}. {self._Computer__make_computations()}"

# Создание объектов и тестирование методов
comp = Computer(15, 8)
print(comp.info())
print("Процессор: ", comp.getteri_cpu())
print("Память:", comp.getteri_memory())

laptop = Laptop(7, 1, 256)
print(laptop.info())
print("Процессор:", laptop.getteri_cpu())
print("Память:", laptop.getteri_memory())
print("Карта памяти:", laptop.get_memory_card())
