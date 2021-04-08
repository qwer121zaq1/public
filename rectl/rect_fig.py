from rect import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_')

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square())
print(square_2.get_area_square())
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_')

cir_1 = Circle(7)
cir_2 = Circle(13)
print(cir_1.get_area_circle())
print(cir_2.get_area_circle())
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_')

figures = [rect_1, rect_2, square_1, square_2, cir_1, cir_2]

for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.get_area())
    elif isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area_circle())
