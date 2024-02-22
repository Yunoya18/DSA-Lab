"""Labs 11.02"""
import json
def selection_sort(lst: list, last):
    """Selection Sort"""
    count = 0
    current = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if lst[walker] < lst[smallest]:
                smallest = walker
            walker += 1
            count += 1
        lst[current], lst[smallest] = lst[smallest], lst[current]
        current += 1
        print(lst)
    print("Comparison times:", count)

selection_sort(json.loads(input()), int(input()))
