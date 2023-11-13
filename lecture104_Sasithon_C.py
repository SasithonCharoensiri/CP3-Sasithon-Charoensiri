class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add to Cart", self.name, self.lastname, "'s cart")

customer1 = Customer()
customer1.name = "Sasithon"
customer1.lastname = "Charoensiri"
customer1.addCart()

customer2 = Customer()
customer2.name = "Waranin"
customer2.lastname = "Chaiyo"
customer2.addCart()

customer3 = Customer()
customer3.name = "Rungthip"
customer3.lastname = "Tiruang"
customer3.addCart()

customer4 = Customer()
customer4.name = "Sasiwimol"
customer4.lastname = "Charoensiri"
customer4.addCart()