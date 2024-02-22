"""Labs 11.04"""
import json
def insertion_sort(lst, last):
    """Insertion Sort"""
    count = 0
    current = 1
    while current <= last:
        hold = lst[current]
        walker = current - 1
        while walker >= 0:
            count += 1
            if hold[0] < lst[walker][0] or\
            (hold[0] == lst[walker][0] and int(hold[1:]) < int(lst[walker][1:])):
                lst[walker], lst[walker+1] = lst[walker+1], lst[walker]
                walker -= 1
            else:
                break
        hold = lst[walker + 1]
        current += 1
        print(lst)
    print("Comparison times:", count)

insertion_sort(json.loads(input()), int(input()))
