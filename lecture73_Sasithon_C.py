systemMenu = {"Orange": 10, "Lemon": 20, "Lime": 30, "Apple": 40}
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
        menuList.append([menuName,systemMenu[menuName]])

showBill()