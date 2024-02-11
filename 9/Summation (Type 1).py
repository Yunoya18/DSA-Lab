"""Labs 09.01"""
def summation(num):
    """sum"""
    current = 1
    total = 0
    while current <= num:
        total += current
        current += 1
    print(total)

summation(int(input()))
