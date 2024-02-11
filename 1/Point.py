"""Lab 01.05 - Point"""
class Point:
    """point information"""
    def __init__(self, point_x=0, point_y=0):
        self.set_coordinates(point_x, point_y)

    def set_coordinates(self, point_x, point_y):
        """set cord"""
        self.point_x = point_x
        self.point_y = point_y

    def get_coordinates(self):
        """return point as tuple"""
        return (self.point_x, self.point_y)

    def calculate_distance(self, other_point):
        """find distance"""
        return ((other_point.point_x - self.point_x)**2\
                + (other_point.point_y - self.point_y)**2) ** 0.5

def main():
    """get info"""
    point_1 = Point(float(input()), float(input()))
    point_2 = Point(float(input()), float(input()))
    distance = point_1.calculate_distance(point_2)
    print("%.2f" % distance)

main()
