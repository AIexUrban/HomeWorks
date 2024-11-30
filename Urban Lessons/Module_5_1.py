class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor) -> None:
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Этажа с номером {new_floor} в "{self.name}"\
c {self.number_of_floors} этажами, не существует.')
        else:
            for i in range (1, new_floor+1):
                print(f'Этаж {i}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)