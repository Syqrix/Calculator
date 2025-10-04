import math
import fractions
from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b=None):
        pass

    @abstractmethod
    def name(self):
        pass


class Addition(Operation):
    def execute(self, a, b=None):
        return a + b

    def name(self):
        return "Addition"


class Subtract(Operation):
    def execute(self, a, b=None):
        return a - b

    def name(self):
        return "Subtraction"


class Multiply(Operation):
    def execute(self, a, b=None):
        return a * b

    def name(self):
        return "Multiplication"


class Divide(Operation):
    def execute(self, a, b=None):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def name(self):
        return "Division"


class Power(Operation):
    def execute(self, a, b=None):
        return a ** b

    def name(self):
        return "Power"


class Sqrt(Operation):
    def execute(self, a, b=None):
        if b is not None:
            raise ValueError("Sqrt accepts only one number")
        return math.sqrt(a)

    def name(self):
        return "Square root"


class Factorial(Operation):
    def execute(self, a, b=None):
        if b is not None:
            raise ValueError("Factorial accepts only one number")
        return math.factorial(int(a))

    def name(self):
        return "Factorial"


class TalkingUser:
    def __init__(self, hi_words="Hello, this is calculator app. Type 'q' anytime to quit.",
                 bye_words="Thanks for using calculator! Bye!"):
        self._hi_words = hi_words
        self._bye_words = bye_words

    def say_hi(self):
        print(self._hi_words)

    def say_bye(self):
        print(self._bye_words)


class UserInput:
    def get_number(self, text="Enter number: "):
        while True:
            number_str: str = input(text)
            if number_str.lower() == "q":
                return None
            if not number_str:
                return number_str
            try:
                return float(number_str)
            except ValueError:
                print("Please enter a valid number!")


class History:
    def __init__(self):
        self.history_of_inputs: list = []

    def show_history(self):
        if not self.history_of_inputs:
            print("The history is empty!")
        else:
            for i in self.history_of_inputs:
                print(i)

    def add_history(self, text: str):
        self.history_of_inputs.append(text)

    def clear_history(self):
        self.history_of_inputs.clear()
        print("History has been cleared!")


class Program:
    def __init__(self, history: History, numbers: UserInput):
        self.history = history
        self.numbers = numbers

    def start_program(self):
        operations = {
            1: self.get_input,
            2: self.history.show_history,
            3: self.history.clear_history,
        }

        print("\nAvailable operations:")
        for key, func in operations.items():
            print(f"{key}: {func.__name__}")

        while True:
            user_answer: str = input("Choose operation: ")
            if user_answer.lower() == "q":
                return None
            if not user_answer.isdigit():
                print("Only numbers! Try again.")
                continue
            user_answer: int = int(user_answer)
            if user_answer not in operations:
                print("Wrong value. Try again!")
                continue
            if user_answer == 2:
                operations[user_answer]()
                continue
            else:
                operations[user_answer]()

    def chose_math_operation(self, a, b):
        operations = {
            1: Addition(),
            2: Subtract(),
            3: Multiply(),
            4: Divide(),
            5: Power(),
            6: Sqrt(),
            7: Factorial(), }

        print("\nAvailable operations:")
        for key, func in operations.items():
            print(f"{key}: {func.name()}")

        while True:
            user_answer: str = input("Choose operation: ")
            if user_answer.lower() == "q":
                return None
            if not user_answer.isdigit():
                print("Only numbers! Try again.")
                continue
            user_answer: int = int(user_answer)
            if user_answer not in operations:
                print("Wrong value. Try again!")
                continue
            op = operations[user_answer]
            if isinstance(op, (Sqrt, Factorial)):
                result = op.execute(a)
                self.history.add_history(f"{op.name()}: {a} = {result}")
            else:
                result = op.execute(a, b)
                self.history.add_history(f"{op.name()}: {a}, {b} = {result}")
            print(f"Result = {result}")
            self.start_program()

    def get_input(self):
        while True:
            first_number = self.numbers.get_number("Enter first number: ")
            if first_number is None:
                break
            second_number = self.numbers.get_number("Enter second number: ")
            if second_number is None:
                break
            if self.chose_math_operation(first_number, second_number) is None:
                break


class Calculator:
    def __init__(self, program: Program, user_comunication: TalkingUser):
        self.user_comunication = user_comunication
        self.program = program

    def run(self):
        self.user_comunication.say_hi()
        self.program.start_program()
        self.user_comunication.say_bye()


def main():
    user_comunication = TalkingUser()
    numbers = UserInput()
    history = History()
    program = Program(history, numbers)
    app = Calculator(program, user_comunication)
    app.run()


if __name__ == "__main__":
    main()
