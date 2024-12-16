def isCorrectRect(arg): #Функция для проверки правильности прямоугольника
    if not isinstance(arg, list) or len(arg) != 2: # Проверка, что аргумент является списком и имеет две точки
        return False
    bottomleft, topright = arg
    # Проверка, что обе точки — это кортежи
    if not (isinstance(bottomleft, tuple) and isinstance(topright, tuple)):
        return False
    if len(bottomleft) != 2 or len(topright) != 2: # Проверка, что каждая из точек состоит из 2 чисел
        return False
    if not all(isinstance(coord, (int, float)) for coord in bottomleft + topright):  #Проверка, что в каждой из точек координаты являются числами
        return False
    return bottomleft[0] < topright[0] and bottomleft[1] < topright[1] # Проверка, что нижний левый угол находится внизу слева относительно верхнего правого

class RectCorrectError(Exception): # Создание пользовательской ошибки если прямоугольник задан неправильно
    pass

def isCollisionRect(peresec1, peresec2): # Функция для проверки пересечения двух прямоугольников
    # Проверка правильности прямоугольников
    if not isCorrectRect(peresec1):
        raise RectCorrectError("1й прямоугольник задан неправильно")
    if not isCorrectRect(peresec2):
        raise RectCorrectError("2й прямоугольник задан неправильно")
    #Извлекаем координаты для каждого прямоугольника
    x1, y1 = peresec1[0]
    x2, y2 = peresec1[1]
    x3, y3 = peresec2[0]
    x4, y4 = peresec2[1]
    
    # Проверка пересечения прямоугольников
    return not (x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1)

def intersectionAreaRect(peresec1, peresec2): # Функция для вычисления площади пересечения двух прямоугольников
    # Проверка корправильностиректности прямоугольников
    if not isCorrectRect(peresec1):
        raise ValueError("1й прямоугольник задан неправильно")
    if not isCorrectRect(peresec2):
        raise ValueError("2й прямоугольник задан неправильно")
    
    # Если правильности не пересекаются
    if not isCollisionRect(peresec1, peresec2):
        return 0
    
    # Вычисление координат пересечения
    x1, y1 = max(peresec1[0][0], peresec2[0][0]), max(peresec1[0][1], peresec2[0][1])
    x2, y2 = min(peresec1[1][0], peresec2[1][0]), min(peresec1[1][1], peresec2[1][1])
    
    # Площадь пересечения
    return (x2 - x1) * (y2 - y1)

def intersectionAreaMultiRect(rectangles):
    from itertools import combinations
    
    # Проверка правильности всех прямоугольников
    if not all(isCorrectRect(rect) for rect in rectangles):
        raise RectCorrectError("Один из прямоугольников задан неправильно")
    
    total_area = 0
    # Перебор всех возможных пар прямоугольников для нахождения пересечений
    for peresec1, peresec2 in combinations(rectangles, 2):
        total_area += intersectionAreaRect(peresec1, peresec2)
    
    return total_area
