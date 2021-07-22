DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if len(customer) == 2:
        return price * (1-customer['discount'])
    return price * (1 - DEFAULT_DISCOUNT)


print(get_discount_price_customer(100, {"name": "Boris", "discount": 0.15}))







