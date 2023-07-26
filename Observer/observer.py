#/bin/python


from abc import ABC, abstractmethod
 
class ObserverInterface(ABC):
 
    def __init__(self, observerName, subject):
        self.subject = subject
        subject.registerObserver(observerName, self)
        super().__init__()
    
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

class DisplayElement:

    @abstractmethod
    def display(self):
        pass


class WeatherDisplay(ObserverInterface, DisplayElement):
    # https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
    def __init__(self, observerName, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        super().__init__(observerName, weatherData)


    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def display(self):
        print ("Temperature: ", self.temperature)
        print ("Humidity: ", self.humidity)
        print ("Pressure: ", self.pressure)



class SubjectInterface(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def registerObserver(name, observer):
        pass

    @abstractmethod
    def removeObserver(name):
        pass

    @abstractmethod
    def notifyObservers(data):
        pass

class WeatherStation(SubjectInterface):
    def __init__(self, temperature, humidity, pressure):
        self.observers = {}

        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        super().__init__()

    def registerObserver(self, name, observer):
        self.observers[name] = observer

    def removeObserver(self, name):
        del self.observers[name]

    def notifyObservers(self):
        print ("notifying observers!")
        for name, observer in self.observers.items():
            observer.update(self.temperature, self.humidity, self.pressure)

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        notifyObservers()




def main():
    print("Hello World!")
    ws = WeatherStation(70, 80, 1.1)
    wd = WeatherDisplay("WeatherDisplay", ws)
    wd.display()
    ws.notifyObservers()
    wd.display()

if __name__ == "__main__":
    main()
