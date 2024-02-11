"""Lab 07.04"""
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

    def is_empty(self):
        """check empty"""
        if self.root == None:
            return True
        else:
            return False

    def preorder(self, root):
        """preorder"""
        if root != None:
            print("->", root.get_data(), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

    def inorder(self, root):
        """inorder"""
        if root != None:
            self.inorder(root.get_left())
            print("->", root.get_data(), end=" ")
            self.inorder(root.get_right())

    def postorder(self, root):
        """postorder"""
        if root != None:
            self.postorder(root.get_left())
            self.postorder(root.get_right())
            print("->", root.get_data(), end=" ")

    def traverse(self, root):
        """traverse"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder(root)
        print()
        print('Inorder: ', end='')
        self.inorder(root)
        print()
        print('Postorder: ', end='')
        self.postorder(root)
        print()

    def find_min(self):
        """min"""
        if self.get_root() == None:
            return None
        else:
            current = self.get_root()
            while current.get_left():
                current = current.get_left()
            return current.get_data()

    def find_max(self):
        """max"""
        if self.get_root() == None:
            return None
        else:
            current = self.get_root()
            while current.get_right():
                current = current.get_right()
            return current.get_data()

def main():
    """main"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse(my_bst.get_root())
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()
