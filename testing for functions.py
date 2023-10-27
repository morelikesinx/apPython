def store():
    Product_Name = str(input('What is your product name?'))
    Product_Price = float(input('What is your product price?'))
    Store_Member = input('Are you a store member?')
    if Store_Member == 'yes':
        discount_25 = Product_Price*.25
        print(Product_Price-discount_25)
    elif Store_Member == 'no':
        Member_Invite = str(input('Would you like to become a member?'))
        if Member_Invite == 'yes':
            discount_10 = Product_Price*.10
            print(Product_Price-discount_10)
        else:
            print('Here is your item price.' + str(Product_Price))

user_word = str(input('What word would you like to reverse?'))
user_reversed = user_word[::-1]
print(user_reversed)