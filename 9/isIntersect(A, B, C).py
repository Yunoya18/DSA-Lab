"""Labs 09.02"""
import json
def isintersect(list_a, list_b, list_c):
    """check"""
    for num in list_a:
        if num in list_b and num in list_c:
            return True
    return False

print(isintersect(json.loads(input()), json.loads(input()), json.loads(input())))

