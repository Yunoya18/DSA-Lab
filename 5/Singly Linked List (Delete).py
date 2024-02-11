"""Lab 05.05"""
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

    def insert_before(self, node, data):
        """add before node"""
        current = self.head
        try:
            if current.get_data() == node:
                self.insert_front(data)
            else:
                while current.get_next() != None:
                    if current.get_next().get_data() == node:
                        break
                    current = current.get_next()
                if current.get_next().get_data() == node:
                    new_node = DataNode(data)
                    new_node.set_next(current.get_next())
                    current.set_next(new_node)
                    self.count += 1
                else:
                    print("Cannot insert, %s does not exist." % node)
        except AttributeError:
            print("Cannot insert, %s does not exist." % node)

    def delete(self, data):
        """delete"""
        current = self.head
        try:
            if current.get_data() == data:
                self.head = current.get_next()
                self.count -= 1
            else:
                while current.get_next() != None:
                    if current.get_next().get_data() == data:
                        break
                    current = current.get_next()
                if current.get_next().get_data() == data:
                    current.set_next(current.get_next().get_next())
                    self.count -= 1
                else:
                    print("Cannot delete, %s does not exist." % data)
        except AttributeError:
            print("Cannot delete, %s does not exist." % data)

def main():
    """test"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()
