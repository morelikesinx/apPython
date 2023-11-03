def TargetStore():
    print('Hello. What is your name?')
NAME = str(input('Enter name here'))
print('Welcome to Target,' + NAME)
print('What item would you like to enter in the register?')
ITEM = str(input('Enter name of item:'))
print('Your product is,' + str(ITEM))
print('What is the price of your item?')
Item_price = float(input('Enter item price:'))
print('Your item price is' + float(Item_price))
COUPON = str(input('Would you like a coupon to get 20 percent off? y or n'))
Discount_20 = Item_price * 0.20
New_Item_price = Item_price-Discount_20
if COUPON == 'y':
    print('Your item price is now' + float(New_Item_price))
elif COUPON == 'n':
    print('Your item price will still be' + float(Item_price))
VERIFICATION = str(input('Are you sure you do not want a coupon? y or n'))
if VERIFICATION == 'y':
    print('Your item price is now' + float(New_Item_price))
elif VERIFICATION == 'n':
    print('Thank you for shopping at Target!')

TargetStore()
