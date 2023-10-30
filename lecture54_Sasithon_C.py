def login():
    username = input("Input Username : ")
    password = input("Input Password : ")
    if username == "customer" and password == "1234":
        return True
    else:
        return False

def showMenu():
    print("------Welcome!!------")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelected():
    userSelected = int(input("Select : "))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculate():
    price1 = int(input("1st Product price : "))
    price2 = int(input("2nd Product price : "))
    return vatCalculate(price1+price2)


if login() == True:
    showMenu()
    userSelect = menuSelected()
    if userSelect == 1:
        inputVatPrice = int(input("Input price (THB) : "))
        print("Your product price is", vatCalculate(inputVatPrice), "THB")
    elif userSelect == 2:
        print("The total price (vat 7%) is", priceCalculate(), "THB")
    else:
        print("It not on menu.")
else :
    print("Username or password incorrect!!...Try again")