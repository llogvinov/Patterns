class Map:
    @staticmethod
    def road(type_road):
        pass


class AutoRoad(Map):
    @staticmethod
    def road(type_road):
        print('Маршрут для авто построен')


class WalkingRoad(Map):
    @staticmethod
    def road(type_road):
        print('Пеший маршрут построен')


class BikeRoad(Map):
    @staticmethod
    def road(type_road):
        print('Маршрут для велопрогулки построен')


class BusRoad(Map):
    @staticmethod
    def road(type_road):
        print('Маршрут на общественном транспорте построен')


class SightRoad(Map):
    @staticmethod
    def road(type_road):
        print('Маршрут по достопримечательностям построен')


class Search:
    def __init__(self, test, type_road):
        self._test = test
        self._type_road = type_road

    @classmethod
    def searching(cls, type_road):
        if type_road == 'авто':
            road_man = AutoRoad
        elif type_road == 'пешком':
            road_man = WalkingRoad
        elif type_road == 'велосипед':
            road_man = BikeRoad
        elif type_road == 'автобус':
            road_man = BusRoad
        elif type_road == 'достопримечательность':
            road_man = SightRoad
        else:
            print('Невозможно найти маршрут для %s' % type_road)
        # Выполнение операции с помощью стратегии:
        test = road_man.road(type_road)
        return cls(test, type_road)


Search.searching(type_road='авто')
Search.searching(type_road='автобус')
Search.searching(type_road='велосипед')
