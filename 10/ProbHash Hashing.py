"""Labs 10.02"""
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

class ProbHash:
    """hash"""
    def __init__(self, size: int):
        self.__hash_table = [[] for _ in range(size)]
        self.__size = size

    def hash(self, key: int):
        """hash"""
        if self.__hash_table[key % self.__size] == []:
            return key % self.__size
        else:
            return self.hash(self.rehash(key))

    def rehash(self, key: int):
        """hash again"""
        return (key + 1) % self.__size

    def insert_data(self, student):
        """insert"""
        if [] in self.__hash_table:
            index = self.hash(student.get_std_id())
            self.__hash_table[index] = student
            print("Insert %d at index %d" % (student.get_std_id(), index))
        else:
            print("The list is full. %d could not be inserted." % student.get_std_id())

    def search_data(self, std_id):
        """"search"""
        for index in range(self.__size):
            if self.__hash_table[index] != []:
                if self.__hash_table[index].get_std_id() == std_id:
                    print("Found %d at index %d" % (std_id, index))
                    return self.__hash_table[index]
        print("%d does not exist." % std_id)

def main():
    """main"""
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
