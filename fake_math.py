class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors # Характиристика


    def __len__(self):
        return self.number_of_floors # для потчета этожей

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.number_of_floors == other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}" #

    def __add__(self, value):
        return self.number_of_floors + value.number_of_floors

    def __radd__(self, value):
        return self.number_of_floors + value.number_of_floors


h1: House = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20) #


print(h1)
print(h2)

print(20 == 20)
print(10 <= 20)
print(10 > 20)
print(10 >= 20)
print(10 != 20)

print(len(h1))
print(len(h2))
#self.name == other.name
#def __lt__(self, other):
    #return self.number_of_floors < other.number_of_floors