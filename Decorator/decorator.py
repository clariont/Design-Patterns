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

    #def __init__(self, wrappedBeverage):
    #    self.wrappedBeverage = wrappedBeverage
    #    print ("Condiment mro", self.wrappedBeverage.mro())
    #    super().__init__()
    def __init__(self):
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
        print ("in DripCoffee constructor, self.cost", self.cost)
        super().__init__()

    def get_description(self):
        return self.description

    def get_cost(self):    
        return self.cost

class Milk(Condiment):
    def __init__(self, wrappedBeverage):
        self.wrappedBeverage = wrappedBeverage
        self.description = "Milk"
        self.cost = 0.5
        print ("mro", self.wrappedBeverage.mro())
        print ("cost", wrappedBeverage.get_cost())
        super().__init__()

    def get_description(self):
        temp = self.wrappedBeverage
        return temp.get_description() + ", " + self.description
        #return self.wrappedBeverage.get_description() + ", " + self.description

    def get_cost(self):    
        return self.cost + self.wrappedBeverage.get_cost()
        #return self.cost + self.wrappedBeverage.cost


def main():
    print("Hello World!")

    coffee = DripCoffee()
    print ("coffee.get_cost(): ", coffee.get_cost())
    print (type(coffee))

    coffeemilk = Milk(DripCoffee)
    print(coffeemilk.get_description())
    print(coffeemilk.get_cost())

if __name__ == "__main__":
    main()
