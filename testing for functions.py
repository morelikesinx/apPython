def giftBagFunc():
    gift_bag = ['']
    user_item = input('Enter an item name')
    gift_bag.append(user_item)

while gift_bag <= 6:
  user_item = input('Enter an item name')
  user_item += 1

  if gift_bag==6:
      print('bag is full')
      print(gift_bag)
giftBagFunc()