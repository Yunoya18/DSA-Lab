"""Lab 07.01"""
class BSTNode:
    """Node"""
    def __init__(self):
        self.data = int
        self.left = None
        self.right = None

    def get_data(self):
        """data getter"""
        return self.data

    def set_data(self, data):
        """data setter"""
        self.data = data

    def get_left(self):
        """left getter"""
        return self.left

    def set_left(self, left):
        """left setter"""
        self.left = left

    def get_right(self):
        """right getter"""
        return self.right

    def set_right(self, right):
        """right setter"""
        self.right = right

P_NEW = BSTNode()
P_NEW.set_data(int(input()))
print(P_NEW.get_data())
print(P_NEW.get_left())
print(P_NEW.get_right())
