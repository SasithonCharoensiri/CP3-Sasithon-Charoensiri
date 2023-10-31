menuList = []

def showBill():
    totalPrice = 0
    print("----My foodland----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        totalPrice += int(menuList[i][1])
    print("Total price =", totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

showBill()
