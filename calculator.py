import math
import fractions
# fdskgf


class Calculator:
    def __init__(self):
        self.history = []

    def say_hi(self):
        print("Hello, this is calculator app. Type 'q' anytime to quit.")

    def get_number(self, text="Enter number: "):
        while True:
            number_str = input(text)
            if number_str.lower() == "q":
                return None
            try:
                return float(number_str)
            except ValueError:
                print("Please enter a valid number!")

    def clear_history(self):
        while True:
            user_answer = input(
                "Do you really want to clear the history? y/n: ")
            if user_answer.lower() == "y":
                break
            else:
                if user_answer.lower() == "n":
                    return None
                if not user_answer:
                    print("It's empty, try again!")
                    continue
                if user_answer.isdigit():
                    print("Only numbers!")
                    continue
        self.history.clear()

    def show_history(self):
        if not self.history:
            print("The history is empty!")
        else:
            for i in self.history:
                print(i)

    def addition(self, a, b):
        self.history.append(f"{a} + {b} = {a + b}")
        print(f"Answer: {a + b}")

    def subtraction(self, a, b):
        self.history.append(f"{a} - {b} = {a - b}")
        print(f"Answer: {a - b}")

    def multiplication(self, a, b):
        self.history.append(f"{a} * {b} = {a * b}")
        print(f"Answer: {a * b}")

    def division(self, a, b):
        try:
            self.history.append(f"{a} / {b} = {a / b}")
            print(f"Answer: {a / b}")
        except ZeroDivisionError:
            print("You can't divide by 0. Try again.")

    def power(self, a, b):
        self.history.append(f"{a} ** {b} = {a ** b}")
        print(f"Answer: {a ** b}")

    def squart(self, a):
        result = math.sqrt(a)
        self.history.append(f"Squart: {a} = {result}")
        print(f"Answer {result}")

    def factorial(self, a):
        result = math.factorial(a)
        self.history.append(f"Factorial: {a} = {result}")
        print(f"Answer {result}")

    def chose_operation(self, a, b):
        operations = {
            1: self.addition,
            2: self.subtraction,
            3: self.multiplication,
            4: self.division,
            5: self.power,
            6: self.squart,
            7: self.factorial,
            8: self.show_history,
            9: self.clear_history, }

        print("\nAvailable operations:")
        for key, func in operations.items():
            print(f"{key}: {func.__name__}")

        while True:
            user_answer = input("Choose operation: ")
            if user_answer.lower() == "q":
                return None
            if not user_answer.isdigit():
                print("Only numbers! Try again.")
                continue
            user_answer = int(user_answer)
            if user_answer not in operations:
                print("Wrong value. Try again!")
                continue
            if user_answer in range(8, 10):
                operations[user_answer]()
            elif ((user_answer in range(6, 8)) and (a and not b)):
                operations[user_answer](a)
            else:
                operations[user_answer](a, b)
            return 0


def main():
    app = Calculator()
    app.say_hi()
    while True:
        first_number = app.get_number("Enter first number: ")
        if first_number is None:
            break
        second_number = app.get_number("Enter second number: ")
        if second_number is None:
            break
        if app.chose_operation(first_number, second_number) is None:
            break
    print("Thanks for using calculator! Bye!")


if __name__ == "__main__":
    main()
