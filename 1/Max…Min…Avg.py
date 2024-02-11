"""Lab 01.02"""
import json
def main():
    """check num"""
    num_list = json.loads(input())
    lowest, highest = num_list[0], num_list[0]
    for num in num_list:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    print((round(highest, 2), round(lowest, 2), round(sum(num_list)/len(num_list), 2)))

main()
