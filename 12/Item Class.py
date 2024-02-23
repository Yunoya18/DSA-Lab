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

def main():
    """main"""
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
