height = int(input("Input height of Piramid : "))
for i in range(height):
    print(" " * ((height-i)-1), "*" * ((i*2)+1))

