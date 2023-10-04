list_of_items=['apple', 'orange', 'book']

apple_price= 1.00
orange_price= 3.00
book_price=10.00

def cart_items():
    newItem_name= input('Enter name of new item')
    newItem_price= float(input('Enter price of new item'))
    list_of_items.append(newItem_name)
    total_price= apple_price + orange_price + book_price + newItem_price
    print(list_of_items)
    print(total_price)
cart_items()