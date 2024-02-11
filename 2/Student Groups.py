"""Lab 02.03"""
class ArrayStack:
    """create stack"""
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """add new data"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """delete latest data"""
        try:
            self.size -= 1
            return self.data.pop()
        except IndexError:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """check if empty"""
        return len(self.data) == 0

    def get_stack_top(self):
        """get latest data"""
        try:
            return self.data[-1]
        except IndexError:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        """get data size"""
        return len(self.data)

    def print_stack(self):
        """print all data"""
        print(self.data)

def main():
    """create group"""
    name = ArrayStack()
    group = int(input())
    student = int(input())
    for _ in range(student):
        name.push(input())
    each_group = [ArrayStack() for _ in range(group)]
    for i in range(name.get_size()):
        each_group[i % group].push(name.pop())
    for num in range(group):
        print("Group " + str(num + 1) + ": " + ", ".join(each_group[num].data))

main()
