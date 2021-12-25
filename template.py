from abc import ABC, abstractmethod


class BaseCut(ABC):
    # последовательность действия одинаковых для всех пирогов и уже определена:
    def haircut(self):
        self._cut_top()
        self._cut_side()
        self._equalize()

    @abstractmethod
    def _cut_top(self):
        pass

    @abstractmethod
    def _cut_side(self):
        pass

    @abstractmethod
    def _equalize(self):
        pass


class ShortCut(BaseCut):
    def _cut_top(self):
        print("Состригаем 1 см")

    def _cut_side(self):
        print("Бреем виски")

    def _equalize(self):
        print("Ровняем челку")


class LongCut(BaseCut):
    def _cut_top(self):
        print("Ровняем кончики")

    def _cut_side(self):
        print("Не трогаем бока")

    def _equalize(self):
        print("Аккуратно задаем пропорции")


shortCut = ShortCut()
longCut = LongCut()

print("Короткая стрижка:")
shortCut.haircut()
print("\nДлинная срижка:")
longCut.haircut()
