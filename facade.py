class CookDish:
    def __init__(self, prep=None, slicing=None, baking=None):
        self._prep = prep or Preparing()
        self._slicing = slicing or Slicing()
        self._baking = baking or Baking()

    def operation(self):
        results = []
        results.append(self._prep.wash_operation())
        results.append(self._prep.cleaning_operation())
        results.append(self._slicing.fix_operation())
        results.append(self._slicing.slice_operation())
        results.append(self._baking.heat_operation())
        results.append(self._baking.fry_operation())
        return '\n'.join(results)


class Preparing:
    def wash_operation(self):
        return 'Моем продукты'

    def cleaning_operation(self):
        return 'Очищаем продукты'


class Slicing:
    def fix_operation(self):
        return 'Отрезаем лишнее'

    def slice_operation(self):
        return 'Нарезаем продукты'


class Baking:
    def heat_operation(self):
        return 'Греем плиту'

    def fry_operation(self):
        return 'Жарим блюдо'

cooking_dish = CookDish()
print(cooking_dish.operation())