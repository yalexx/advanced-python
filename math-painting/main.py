from reportlab.pdfgen import canvas


class Canvas:
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

    def draw(self, canvas):
        pass


class Rectangle:
    def __init__(self, x, y, a, b, color):
        self.color = color
        self.b = b
        self.a = a
        self.y = y
        self.x = x

    def draw(self, canvas):
        pass


class Square:
    def __init__(self, x, y, a, color):
        self.color = color
        self.a = a
        self.y = y
        self.x = x

    def draw(self, canvas):
        pass


canvas1 = Canvas(100, 100, 'red')
rect1 = Rectangle(100, 100, 100, 100, 'red')
rect1.draw(canvas1)

