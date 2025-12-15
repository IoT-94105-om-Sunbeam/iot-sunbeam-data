def order(item, quantity=1, price=50):
    total = quantity * price
    print("Item:", item)
    print("Total Price:", total)

order("Pen")
order("Book", quantity=3)
order("Notebook", price=40, quantity=5)