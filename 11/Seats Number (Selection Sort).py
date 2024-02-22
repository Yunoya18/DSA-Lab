"""Labs 11.05"""
import json
def selection_sort(lst: list, last):
    """Selection Sort"""
    count = 0
    current = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if lst[walker][0] < lst[smallest][0] or\
            (lst[walker][0] == lst[smallest][0] and int(lst[walker][1:]) < int(lst[smallest][1:])):
                smallest = walker
            walker += 1
            count += 1
        lst[current], lst[smallest] = lst[smallest], lst[current]
        current += 1
        print(lst)
    print("Comparison times:", count)

selection_sort(json.loads(input()), int(input()))
