"""Labs 11.03"""
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
            if lst[walker] < lst[walker-1]:
                sort = False
                lst[walker], lst[walker-1] = lst[walker-1], lst[walker]
            walker -= 1
            count += 1
        current += 1
        print(lst)
    print("Comparison times:", count)

bubble_sort(json.loads(input()), int(input()))
