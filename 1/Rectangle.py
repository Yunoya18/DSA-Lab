"""Lab 01.04 - Rectangle"""
class Rectangle:
    """rectangle information"""
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        """find area"""
        return self.width * self.height

    def calculate_perimeter(self):
        """find perimeter"""
        return (self.width + self.height) * 2

def main(height, width, condition):
    """check condition"""
    if condition == "area":
        result = Rectangle(height, width).calculate_area()
    else:
        result = Rectangle(height, width).calculate_perimeter()
    print("%.2f" % result)

main(float(input()), float(input()), input())
