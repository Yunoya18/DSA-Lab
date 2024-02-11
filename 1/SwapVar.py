"""Lab 01.03 - SwapVar"""
def convert_to_tuples(text_in):
    """convert input"""
    values = text_in.strip('()').split(', ')
    values[0], values[1] = values[1], values[0]
    print(tuple(map(float, values)))

convert_to_tuples(input())
