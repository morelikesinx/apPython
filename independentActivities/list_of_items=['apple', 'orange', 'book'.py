data= input('input a data type. ')

hi= type(data)

def datatype(data):
    if hi == str(data):
        print('That is a string')
    elif hi == int(data):
        print("that is an integer")
    if hi == float(data):
        print('That is a float')

datatype(data)