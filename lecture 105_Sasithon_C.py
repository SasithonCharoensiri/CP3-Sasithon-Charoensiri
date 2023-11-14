class Vehecle:
    licenseNumber = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehecle):
    def sayHello(self):
        print("Hello World")

class PickUp(Vehecle):
    pass

class Van(Vehecle):
    pass

class Estatecar(Vehecle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()

