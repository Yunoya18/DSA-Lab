"""Lab 05.03"""
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

class SinglyLinkedList:
    """create linked list"""
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        """traverse list"""
        if self.count == 0:
            print("This is an empty list.")
        else:
            current = self.head
            while current != None:
                print(current.get_data(), end="")
                if current.get_next() != None:
                    print(" -> ", end="")
                current = current.get_next()

    def insert_last(self, data):
        """add last"""
        new_node = DataNode(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
        self.count += 1

    def insert_front(self, data):
        """add front"""
        new_node = DataNode(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

LIST1_ = SinglyLinkedList()
for _ in range(int(input())):
    TEXT_ = input()
    CONDI_, DATA_ = TEXT_.split(": ")
    if CONDI_ == "F":
        LIST1_.insert_front(DATA_)
    elif CONDI_ == "L":
        LIST1_.insert_last(DATA_)
    else:
        print("Invalid Condition!")
LIST1_.traverse()
