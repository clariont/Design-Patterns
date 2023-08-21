#/bin/python


from abc import ABC, abstractmethod

class Beverage(ABC):
 
    def __init__(self):
        #super().__init__()
        pass
    
    def get_description(self):
        return self.description

    @abstractmethod
    def get_cost(self):
        pass
 
class Condiment(Beverage):

    def __init__(self, wrappedBeverage):
        self.wrappedBeverage = wrappedBeverage
        super().__init__()
    
    @abstractmethod
    def get_description(self):
        return self.description

    @abstractmethod
    def get_cost(self):
        pass

class DripCoffee(Beverage):
    def __init__(self):
        self.description = "Drip Coffee"
        self.cost = 3.0
        super().__init__()

    def get_description(self):
        return self.description

    def get_cost(self):    
        return self.cost


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
        self.cost = 2.5
        super().__init__()

    def get_description(self):
        return self.description

    def get_cost(self):    
        return self.cost


class WholeMilk(Condiment):
    def __init__(self, wrappedBeverage):
        self.wrappedBeverage = wrappedBeverage
        self.description = "WholeMilk"
        self.cost = 0.25
        super().__init__(self.wrappedBeverage)

    def get_description(self):
        return self.wrappedBeverage.get_description() + ", " + self.description

    def get_cost(self):    
        return self.wrappedBeverage.get_cost() + self.cost

class Vanilla(Condiment):
    def __init__(self, wrappedBeverage):
        self.wrappedBeverage = wrappedBeverage
        self.description = "Vanilla"
        self.cost = 0.5
        super().__init__(self.wrappedBeverage)

    def get_description(self):
        return self.wrappedBeverage.get_description() + ", " + self.description

    def get_cost(self):    
        return self.wrappedBeverage.get_cost() + self.cost


class OatMilk(Condiment):
    def __init__(self, wrappedBeverage):
        self.wrappedBeverage = wrappedBeverage
        self.description = "OatMilk"
        self.cost = 1.0
        super().__init__(self.wrappedBeverage)

    def get_description(self):
        return self.wrappedBeverage.get_description() + ", " + self.description

    def get_cost(self):    
        return self.wrappedBeverage.get_cost() + self.cost

def printBeverage(beverage):
    print ("Your order is ", beverage.get_description(), " and the cost is: ", beverage.get_cost())


def main():
    print("Hello World!")

    coffeemilk = WholeMilk(DripCoffee())
    printBeverage(coffeemilk)
    printBeverage(Vanilla(OatMilk(Espresso())))

if __name__ == "__main__":
    main()
