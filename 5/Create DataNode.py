"""Lab 05.01"""
class DataNode:
    """create data node"""
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def get_data(self):
        """data getter"""
        return self.__data

    def set_data(self, data):
        """data setter"""
        self.__data = data

    def get_next(self):
        """next getter"""
        return self.__next

    def set_next(self, node):
        """next setter"""
        self.__next = node

NODE_ = DataNode(input())
print(NODE_.get_data())
print(NODE_.get_next())
