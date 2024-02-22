"""Labs 11.06"""
import json
def bubble_sort(lst, last):
    """Bubble Sort"""
    count = 0
    current = 0
    sort = False
    while current <= last and sort == False:
        walker = last
        sort = True
        while walker > current:
            if lst[walker][0] < lst[walker-1][0] or\
            (lst[walker][0] == lst[walker-1][0] and int(lst[walker][1:]) < int(lst[walker-1][1:])):
                sort = False
                lst[walker], lst[walker-1] = lst[walker-1], lst[walker]
            walker -= 1
            count += 1
        current += 1
        print(lst)
    print("Comparison times:", count)

bubble_sort(json.loads(input()), int(input()))
