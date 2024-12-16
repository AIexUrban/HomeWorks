
class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled = bool):
        self.__sides = [sides for i in range(self.sides_count)]
        self.__color = list(color)
        self.filled = filled


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
             return True if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 else False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r,g,b]

    def __is_valid_sizes(self, *args: list):
        return True if (all(map(lambda x: x > 0, args))
                    and len(args) == self.sides_count) else False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sizes(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color = color, sides = sides)
        self.__radius =  sides / 2 * 3,1415926
        self.__sides = sides

    def get_square(self):
        #return 3,1415926 * (self.__radius ** 2)
        return self.__sides **2 / (4 * 3,1415926)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color = color, sides = sides)

    def get_square(self, sides):
        a, b, c = self.get_sides()[0], self.get_sides()[1], self.get_sides()[2]
        s = (a + b + c) / 2
        square = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Вычисляем площадь
        return round(square, 2)

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides

    def get_volume(self):
        return self.__sides **3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle1 = Triangle((25,50,255), 20)
    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))
    # Проверка объёма (куба):
    print(cube1.get_volume())
    print('-'*20)
    print(triangle1.get_color())
    print(triangle1.get_square(15))
    triangle1.set_color(27, 29, 280)
    print(triangle1.get_color())  # Не изменится

# END