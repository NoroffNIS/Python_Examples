from polygon import*

class Rectangle(Polygon):
    def set_values(self, width, height):
        self.height = width
        self.width = height

    def area(self):
        return self.width / self.height