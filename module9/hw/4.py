def discount_price(discount):
    def inner(x):
        return x * (1 - discount)
    return inner

cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_05(price))
print(cost_10(price))
print(cost_15(price))