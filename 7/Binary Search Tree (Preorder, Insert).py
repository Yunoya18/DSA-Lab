"""Lab 07.02"""
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

class BST:
    """bst"""
    def __init__(self):
        self.root = None

    def get_root(self):
        """root getter"""
        return self.root

    def set_root(self, root):
        """root setter"""
        self.root = root

    def insert(self, data):
        """insert root"""
        new_node = BSTNode()
        new_node.set_data(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.get_root()
            while current:
                if data < current.get_data():
                    if current.get_left() == None:
                        current.set_left(new_node)
                        break
                    current = current.get_left()
                else:
                    if current.get_right() == None:
                        current.set_right(new_node)
                        break
                    current = current.get_right()

    def preorder(self, root):
        """preorder"""
        if root != None:
            print("->", root.get_data(), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

def main():
    """main"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    print("Preorder: ", end="")
    my_bst.preorder(my_bst.get_root())

main()
