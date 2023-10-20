username = input("Input Username : ")
password = input("Input Password : ")
if username == "customer" and password == "1234":
    print("------Welcome!!------")
    print("What you want to buy ?")
    print("1. Lottary     price : 80 THB")
    print("2. News paper  price : 35 THB")
    print("3. Magazine    price : 50 THB")
    userSelect = int(input("Select : "))

    print("How much do you want?")
    amount = int(input("Amount : "))

    if userSelect == 1:
        print("You buy a Lottary", amount,"piece")
        print("Total :", 80 * amount, "THB")
    elif userSelect == 2:
        print("You buy a News paper", amount, "piece")
        print("Total :", 35 * amount, "THB")
    elif userSelect == 3:
        print("You buy a Magazine", amount, "piece")
        print("Total :", 50 * amount, "THB")
    else:
        print("It not on our menu...")