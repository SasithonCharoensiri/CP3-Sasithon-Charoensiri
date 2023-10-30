def vatCalculator(price):
    result = price+(price*7/100)
    return result

priceInput = int(input("Input price : "))
print(vatCalculator(priceInput))