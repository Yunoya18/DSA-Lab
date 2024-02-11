"""Lab 01.01 - Is_Even"""
def is_even(num):
    check = ["0", "2", "4", "6", "8"]
    if num[-1] in check:
        print(True)
    else:
        print(False)

is_even(input())
