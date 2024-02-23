"""Labs 12.01"""
import json
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def coin_exchange(amount, coins):
    """exchange"""
    data = convert_key(coins)
    result = {}
    left = amount
    for item in data.keys():
        use = min(left//item, data[item])
        result[item] = use
        left -= use * item
    print("Amount:", amount)
    if left:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        total = 0
        for key, value in result.items():
            total += value
            print(" ", key, "baht =", value, "coins")
        print("Number of coins:", total)

coin_exchange(int(input()), json.loads(input()))
