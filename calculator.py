import math
import fractions


class Calculator:
    def __init__(self):
        self.user_comunication = TalkingUser()
        self.program = Operations()

    def run(self):
        self.user_comunication.say_hi()
        self.program.start_program()
        self.user_comunication.say_bye()


class TalkingUser:
    def say_hi(self):
        print("Hello, this is calculator app. Type 'q' anytime to quit.")

    def say_bye(self):
        print("Thanks for using calculator! Bye!")


class UserInput:
    def get_number(self, text="Enter number: "):
        while True:
            number_str = input(text)
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
        self.history_of_inputs = []

    def show_history(self):
        if not self.history_of_inputs:
            print("The history is empty!")
        else:
            for i in self.history_of_inputs:
                print(i)
        self.start_program()

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
        self.history_of_inputs.clear()
        self.start_program()


class Operations(History):
    def __init__(self):
        self.numbers = UserInput()
        self.history_of_inputs = []

    def addition(self, a, b):
        try:
            self.history_of_inputs.append(f"{a} + {b} = {a + b}")
            print(f"Answer: {a + b}")
        except TypeError:
            if a:
                self.history_of_inputs.append(
                    f"For make a sum should be 2 number: Answer is {a}")
                print(f"Answer: {int(a)}")
            if b:
                self.history_of_inputs.append(
                    f"For make a sum should be 2 number: Answer is {b}")
                print(f"Answer: {int(b)}")

    def subtraction(self, a, b):
        try:
            self.history_of_inputs.append(f"{a} - {b} = {a - b}")
            print(f"Answer: {a - b}")
        except TypeError:
            if a:
                self.history_of_inputs.append(
                    f"For make a subtraction should be 2 number: Answer is {a}")
                print(f"Answer: {int(a)}")
            if b:
                self.history_of_inputs.append(
                    f"For make a subtraction should be 2 number: Answer is {b}")
                print(f"Answer: {int(b)}")

    def multiplication(self, a, b):
        try:
            self.history_of_inputs.append(f"{a} * {b} = {a * b}")
            print(f"Answer: {a * b}")
        except TypeError:
            if a:
                self.history_of_inputs.append(
                    f"For make a multiplication should be 2 number: Answer is {a}")
                print(f"Answer: {int(a)}")
            if b:
                self.history_of_inputs.append(
                    f"For make a multiplication should be 2 number: Answer is {b}")
                print(f"Answer: {int(b)}")

    def division(self, a, b):
        try:
            self.history_of_inputs.append(f"{a} / {b} = {a / b}")
            print(f"Answer: {a / b}")
        except ZeroDivisionError:
            print("You can't divide by 0. Try again.")
        except TypeError:
            if a:
                self.history_of_inputs.append(
                    f"For make a division should be 2 number: Answer is {a}")
                print(f"Answer: {int(a)}")
            if b:
                self.history_of_inputs.append(
                    f"For make a division should be 2 number: Answer is {b}")
                print(f"Answer: {int(b)}")

    def power(self, a, b):
        try:
            self.history_of_inputs.append(f"{a} ** {b} = {a ** b}")
            print(f"Answer: {a ** b}")
        except TypeError:
            if a:
                self.history_of_inputs.append(
                    f"For make a power should be 2 number: Answer is {a}")
                print(f"Answer: {int(a)}")
            if b:
                self.history_of_inputs.append(
                    f"For make a power should be 2 number: Answer is {b}")
                print(f"Answer: {int(b)}")

    def squart(self, a, b):
        if a:
            result = math.sqrt(a)
            self.history_of_inputs.append(f"Squart: {a} = {int(result)}")
            print(f"Answer {result}")
        if b:
            result = math.sqrt(b)
            self.history_of_inputs.append(f"Squart: {b} = {int(result)}")
            print(f"Answer {result}")
        if a and b:
            print("Only one number! Please try again")

    def factorial(self, a, b):
        if a:
            a = int(a)
            result = math.factorial(a)
            self.history_of_inputs.append(f"Factorial: {a} = {result}")
            print(f"Answer {result}")
        if b:
            b = int(b)
            result = math.factorial(b)
            self.history_of_inputs.append(f"Factorial: {b} = {result}")
            print(f"Answer {result}")
        if a and b:
            print("Only one number! Please try again")

    def start_program(self):
        operations = {
            1: self.get_input,
            2: self.show_history,
            3: self.clear_history,
        }

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
            operations[user_answer]()
            return 0

    def chose_math_operation(self, a, b):
        operations = {
            1: self.addition,
            2: self.subtraction,
            3: self.multiplication,
            4: self.division,
            5: self.power,
            6: self.squart,
            7: self.factorial, }

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
            elif ((user_answer in range(6, 8)) and (a and not b)):
                operations[user_answer](a)
            else:
                operations[user_answer](a, b)
            return 0

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


def main():
    app = Calculator()
    app.run()


if __name__ == "__main__":
    main()
