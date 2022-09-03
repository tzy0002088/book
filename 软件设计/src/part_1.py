class WaterHeater:
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature
    
    def set_temperature(self,temperature):
        self.__temperature = temperature
        print("当前温度是: " + str(self.__temperature) + "C")
        self.notifies()
    
    def add_observer(self,observer):
        self.__observers.append(observer)
    
    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Washi_mode(object):

    def update(self,waterheater):
        if waterheater.get_temperature() > 50 and waterheater.get_temperature() < 80:
            print("赶紧来洗澡吧")

class Drink_mode(object):

    def update(self,waterheater):
        if waterheater.get_temperature() >= 100:
            print("赶紧来喝水吧")


if __name__  == "__main__":
    header = WaterHeater()
    washobser = Washi_mode()
    drinkobser = Drink_mode()
    header.add_observer(washobser)
    header.add_observer(drinkobser)
    header.set_temperature(70)
    header.set_temperature(120)



