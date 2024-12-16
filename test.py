from collision.main import ( #импорт необходимых функции и классов из модуля collision.main
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect,
    RectCorrectError,
)

def main(): # гл функция, которая демонстрирует использование всех функ
    peresec1 = [(-3, 1), (9, 10)]
    peresec2 = [(-7, 0), (13, 12)]

    # Проверка на правильности прямоугольников
    print(f"Прямоугольник 1 правильный: {isCorrectRect(peresec1)}")
    print(f"Прямоугольник 2 правильный: {isCorrectRect(peresec2)}")

    # Проверка на пересечение
    try:
        result = isCollisionRect(peresec1, peresec2)
        print(f"Пересекаются ли прямоугольники: {result}")
    except RectCorrectError as exe:
        print(f"Ошибка: {exe}")

    #Площадь пересечения двух прямоугольников
    try:
        intersection_area = intersectionAreaRect(peresec1, peresec2)
        print(f"Площадь пересечения: {intersection_area}")
    except ValueError as exe:
        print(f"Ошибка: {exe}")

    rectangles = [ #Пример нескольких прямоугольников для вычисления общей площади пересечений
        [(-3, 1), (9, 10)],
        [(-7, 0), (13, 12)],
        [(0, 0), (5, 5)],
        [(2, 2), (7, 7)]
    ]
    try:
        total_area = intersectionAreaMultiRect(rectangles)
        print(f"Общая площадь пересечения: {total_area}")
    except RectCorrectError as exe:
        print(f"Ошибка: {exe}")

if __name__ == "__main__": # Проверка, если данный скрипт запускается как главный
    main()
