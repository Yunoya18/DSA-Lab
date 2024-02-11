"""Lab 02.05"""
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

def is_parentheses_matching():
    """check if match"""
    text = input()
    data_check = ArrayStack()
    for cha in text:
        if cha == "(":
            data_check.push("(")
        elif cha == ")":
            data_check.pop()
    check = text.count("(") == text.count(")") and data_check.is_empty()
    if check:
        print("Parentheses in " + text + " are matched")
    else:
        print("Parentheses in " + text + " are unmatched")
    print(check)

is_parentheses_matching()
