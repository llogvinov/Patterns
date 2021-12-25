class FahrenheitSensor:
    @staticmethod
    def get_Fahr_temp():
        return 5


class Sensor:
    def get_temp(self):
        pass


class Adapter(Sensor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def get_temp(self):
        return (self.adaptee.get_Fahr_temp() - 32) * 5 / 9


fahr_sensor = FahrenheitSensor()
print(f'Температура в Фаренгейтах\n{fahr_sensor.get_Fahr_temp()}')

sensor = Sensor()

adapter = Adapter(FahrenheitSensor)
print(f'Температура в Цельсиях\n{adapter.get_temp()}')
