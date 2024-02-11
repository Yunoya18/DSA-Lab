"""Lab 01.06 - Elevator"""
class Elevator:
    """set elevator"""
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """set current floor"""
        self.current_floor = floor

    def report_current_floor(self):
        """final floor"""
        print(self.current_floor)

def main():
    """get info"""
    max_floor = int(input())
    elevator = Elevator(max_floor)
    while True:
        floor = input()
        if floor == "Done":
            elevator.report_current_floor()
            break
        elif int(floor) > max_floor:
            print("Invalid Floor!")
        else:
            elevator.go_to_floor(int(floor))

main()
