import math

class GeometryCalculator:
    @staticmethod
    def circle_area(radius):
        """
        Вычисляет площадь круга по заданному радиусу.

        Параметры:
        radius (float): Радиус круга.

        Возвращает:
        float: Площадь круга.
        """
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        """
        Вычисляет площадь треугольника по заданным сторонам с использованием формулы Герона.

        Параметры:
        side1 (float): Длина первой стороны треугольника.
        side2 (float): Длина второй стороны треугольника.
        side3 (float): Длина третьей стороны треугольника.

        Возвращает:
        float: Площадь треугольника.
        """
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Пример использования библиотеки
radius = 5
print("Площадь круга с радиусом", radius, ":", GeometryCalculator.circle_area(radius))

side1 = 3
side2 = 4
side3 = 5
print("Площадь треугольника со сторонами", side1, ",", side2, "и", side3, ":", GeometryCalculator.triangle_area(side1, side2, side3))
