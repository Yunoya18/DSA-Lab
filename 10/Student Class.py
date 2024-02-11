"""Labs 10.01"""
class Student:
    """student info"""
    def __init__(self, std_id: int, name: str, gpa: float):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self):
        """get id"""
        return self.__std_id

    def get_name(self):
        """get name"""
        return self.__name

    def get_gpa(self):
        """get gpa"""
        return self.__gpa

    def print_details(self):
        """print details"""
        print("ID: %d" % self.get_std_id())
        print("Name: %s" % self.get_name())
        print("GPA: %.2f" % self.get_gpa())

def main(text_in):
    """main"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())
