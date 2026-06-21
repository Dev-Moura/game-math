from random import randint


class Calc:
    OPERATORS = {
        1: ("+", lambda a, b: a + b),
        2: ("-", lambda a, b: a - b),
        3: ("*", lambda a, b: a * b),
    }

    def __init__(self, difficulty: int) -> None:
        self.__difficulty = difficulty

        self.__value1 = self._generate_value()
        self.__value2 = self._generate_value()

        self.__operator = randint(1, 3)

        self.__result = self._generate_result()

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @property
    def value1(self) -> int:
        return self.__value1

    @property
    def value2(self) -> int:
        return self.__value2

    @property
    def operator(self) -> int:
        return self.__operator

    @property
    def result(self) -> int:
        return self.__result

    def _generate_value(self) -> int:
        ranges = {1: 10, 2: 100, 3: 1000, 4: 10000}

        max_value = ranges.get(self.difficulty, 100000)
        return randint(0, max_value)

    def _generate_result(self) -> int:
        _, operation = self.OPERATORS[self.operator]
        return operation(self.value1, self.value2)

    @property
    def _operator_symbol(self) -> str:
        symbol, _ = self.OPERATORS[self.operator]
        return symbol

    def show_operation(self) -> None:
        print(f"{self.value1} {self._operator_symbol} {self.value2} = ?")

    def check_answer(self, answer: int) -> bool:
        if answer == self.result:
            print("Correct Answer")
            correct = True
        else:
            print("Wrong Answer")
            correct = False

        print(f"{self.value1} {self._operator_symbol} {self.value2} = {self.result}")

        return correct

    def __str__(self) -> str:
        return f"{self.value1} {self._operator_symbol} {self.value2}"
