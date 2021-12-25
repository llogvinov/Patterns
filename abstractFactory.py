from abc import ABC, abstractmethod
from singleton import SingletonMeta

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_engine(self):
        pass


class AbstractEngine(ABC):
    def __init__(self):
        self.max_speed: int = 0


class AbstractCar(ABC):
    def __init__(self, name):
        self.name: str = name

    @abstractmethod
    def max_speed(self, engine: AbstractEngine):
        pass

    def __str__(self):
        return f'Автомобиль {self.name}'


class FordCar(AbstractCar):
    def __init__(self, name):
        super().__init__(name)

    def max_speed(self, engine: AbstractEngine):
        return engine.max_speed


class FordEngine(AbstractEngine):
    def __init__(self):
        self.max_speed = 220


class AudiCar(AbstractCar):
    def __init__(self, name, body_type):
        super().__init__(name)
        self.body_type = body_type

    def max_speed(self, engine: AbstractEngine):
        return engine.max_speed

    def __str__(self):
        return f'Автомобиль {self.name} с кузовом {self.body_type}'


class AudiEngine(AbstractEngine):
    def __init__(self):
        self.max_speed = 250


class FordFactory(CarFactory, metaclass=SingletonMeta):
    def create_car(self):
        return FordCar('Форд')

    def create_engine(self):
        return FordEngine()


class AudiFactory(CarFactory):
    def create_car(self):
        return AudiCar('Ауди', 'универсал')

    def create_engine(self):
        return AudiEngine()


class Client:
    def __init__(self, car_factory: CarFactory):
        self.abstract_car: AbstractCar = car_factory.create_car()
        self.abstract_engine: AbstractEngine = car_factory.create_engine()

    def run_max_speed(self):
        return self.abstract_car.max_speed(self.abstract_engine)

    def __str__(self):
        return self.abstract_car.__str__()


ford_car = FordFactory()
audi_car = AudiFactory()
client1 = Client(ford_car)
client2 = Client(audi_car)
print(f"Максимальная скорость {client1} состовляет {client1.run_max_speed()} км/час")
print(f"Максимальная скорость {client2} состовляет {client2.run_max_speed()} км/час")
