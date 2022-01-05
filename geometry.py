from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x \
                < rectangle.upright.x \
                and rectangle.lowleft.y < self.y \
                < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright


rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

user_point = Point(float(input('Guess X:')),
                    float(input('Guess Y:')))

print('Your points are inside rectangle: ',
      user_point.falls_in_rectangle(rectangle))
