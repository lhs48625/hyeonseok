def quote(price, quantity, shipping=3000):
    subtotal = price * quantity
    return subtotal + shipping

total = quote(8000, 3)

print(total)
print(quote(8000, 3, shipping=0))