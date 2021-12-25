from abc import ABC, abstractmethod


class ArithmeticUnit:
    def __init__(self):
        self.register = 0

    def run(self, operation_code, operand):
        if operation_code == "+":
            self.register += operand
        elif operation_code == "-":
            self.register -= operand
        elif operation_code == '*':
            self.register *= operand
        elif operation_code == "/":
            self.register /= operand


class Command(ABC):
    def __init__(self, unit, operand):
        self.unit: ArithmeticUnit = unit
        self.operand: float = operand

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def un_execute(self):
        pass


class ControlUnit:
    def __init__(self):
        self.commands = []
        self.current = 0

    def store_command(self, command):
        self.commands.append(command)

    def execute_command(self):
        self.commands[self.current].execute()

    def undo(self):
        self.commands[self.current - 1].un_execute()

    def redo(self):
        self.commands[self.current - 1].execute()


class Add(Command):
    def __init__(self, unit: ArithmeticUnit, operand: float):
        super().__init__(unit, operand)

    def execute(self):
        self.unit.run('+', self.operand)

    def un_execute(self):
        self.unit.run('-', self.operand)


class Calculator:
    def __init__(self):
        self.arithmetic_unit = ArithmeticUnit()
        self.control_unit = ControlUnit()

    def run(self, command: Command) -> float:
        self.control_unit.store_command(command)
        self.control_unit.execute_command()
        return self.arithmetic_unit.register

    def add(self, operand):
        return self.run(Add(self.arithmetic_unit, operand))


calculator = Calculator()
result = calculator.add(5)
print(result)
