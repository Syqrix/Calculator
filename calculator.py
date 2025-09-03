class Calculator:
    def say_hi(self):
        print("Hello, this is calculator app. Type 'q' anytime to quit.")

    def get_number(self, text="Enter number: "):
        while True:
            number_str = input(text)
            if number_str.lower() == "q":
                return None
            try:
                return float(number_str)  # поддержка дробей
            except ValueError:
                print("Please enter a valid number!")

    def addition(self, a, b):
        print(f"Answer: {a + b}")

    def subtraction(self, a, b):
        print(f"Answer: {a - b}")

    def multiplication(self, a, b):
        print(f"Answer: {a * b}")

    def division(self, a, b):
        try:
            print(f"Answer: {a / b}")
        except ZeroDivisionError:
            print("You can't divide by 0. Try again.")

    def power(self, a, b):
        print(f"Answer: {a ** b}")

    def chose_operation(self, a, b):
        operations = {
            1: self.addition,
            2: self.subtraction,
            3: self.multiplication,
            4: self.division,
            5: self.power}

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
