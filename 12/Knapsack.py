"""Labs 12.02"""
class Item:
    """Item info"""
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        """name getter"""
        return self.__name

    def get_price(self):
        """price getter"""
        return self.__price

    def get_weight(self):
        """weght getter"""
        return self.__weight

    def get_cost(self):
        """cost getter"""
        return self.__price/self.__weight

def knapsack(item_lst: list, amount):
    """knapsack"""
    total = 0
    item_lst.sort(key=lambda x: x.get_cost(), reverse=True)
    print("Knapsack Size:", amount, "kg")
    print("===============================")
    for item in item_lst:
        if item.get_weight() < amount:
            total += item.get_price()
            amount -= item.get_weight()
            print(item.get_name(), "->", item.get_weight(), "kg", "->", item.get_price(), "THB")
        else:
            break
    print("Total:", total, "THB")

def main():
    """main"""
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)

main()
