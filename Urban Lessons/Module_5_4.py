"""
class Example:
  def __new__(cls, *args, **kwargs):
    print(args)
    print(kwargs)
    return object.__new__(cls)


  def __init__(self, first, second, third, fourth):
    print(first)
    print(second)
    print(third)
    print(fourth)


ex = Example('data', 'Hi', third=3.14, fourth="Hello")
"""


class House:
  houses_history = []

  def __new__(cls, *args):
    cls.houses_history.append(args[0])
    return object.__new__(cls)

  def __init__(self, name, number_of_floors):
    self.name = name
    self.number_of_floors = number_of_floors

  #     def go_to(self, new_floor) -> None:
  #         if new_floor > self.number_of_floors or new_floor < 1:
  #             print(f'Этажа с номером {new_floor} в "{self.name}"\
  # c {self.number_of_floors} этажами, не существует.')
  #         else:
  #             for i in range (1, new_floor+1):
  #                 print(f'Этаж {i}')
  #

  def __del__(self):
    print(f'{self.name} снесён, но он останется в истории')

  def __len__(self):
    return self.number_of_floors

  def __str__(self):
    return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'

  def __eq__(self, other):  # (=)
    if (isinstance(other, (int, House)) and
            self.number_of_floors == other.number_of_floors):
      return True
    else:
      return False

  def __lt__(self, other):  # (<)
    if (isinstance(other, (int, House)) and
            self.number_of_floors < other.number_of_floors):
      return True
    else:
      return False

  def __le__(self, other):  # (<=)
    if (isinstance(other, (int, House)) and
            self.number_of_floors <= other.number_of_floors):
      return True
    else:
      return False

  def __gt__(self, other):  # (>)
    if (isinstance(other, (int, House)) and
            self.number_of_floors > other.number_of_floors):
      return True
    else:
      return False

  def __ge__(self, other):  # ( >=)
    if (isinstance(other, (int, House)) and
            self.number_of_floors >= other.number_of_floors):
      return True
    else:
      return False

  def __ne__(self, other):  # (!=)
    if (isinstance(other, (int, House)) and
            self.number_of_floors != other.number_of_floors):
      return True
    else:
      return False

  def __add__(self, value):  # увеличение
    if isinstance(value, int and House):
      self.number_of_floors += value.number_of_floors
      return self
    else:
      self.number_of_floors += value
      return self

  def __radd__(self, value):
    if isinstance(value, int and House):
      self.number_of_floors += value.number_of_floors
      return self
    else:
      self.number_of_floors += value
      return self

  def __iadd__(self, value):
    if isinstance(value, int and House):
      self.number_of_floors += value.number_of_floors
      return self
    else:
      self.number_of_floors += value
      return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# END
