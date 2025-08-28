import math


class calculator:
    def say_hi(self):
        print("Hello, this is calculator app. You can type q to leave.")

    def first_user_number(self):
        while True:
            # Разобраться со страпами
            number_str = input("Enter first number: ")
            if number_str.lower() == "q":
                return None
            else:
                if not number_str:
                    print("You have empty space, please repeat operation.")
                    continue

                if number_str.isdigit():
                    number = int(number_str)
                else:
                    print("Please enter the number!")
                    continue
                return number

    def second_user_number(self):
        while True:
            # Разобраться со страпами
            number_str = input("Enter second number: ")
            if number_str.lower() == "q":
                return None
            else:
                if not number_str:
                    print("You have empty space, please repeat operation.")
                    continue

                if number_str.isdigit():
                    number = int(number_str)
                else:
                    print("Please enter the number!")
                    continue
                return number

    def addition(self, first_num, second_num):
        print(f"Answer: {first_num + second_num}")

    def substraction(self, first_num, second_num):
        print(f"Answer: {first_num - second_num}")

    def multiplication(self, first_num, second_num):
        print(f"Answer: {first_num * second_num}")

    def division(self, first_num, second_num):
        try:
            print(f"Answer: {first_num / second_num}")
        except ZeroDivisionError:
            print("You can't divide by 0. Try again.")

    def chose_operation(self, first_number, second_number):
        operations = {1: "addition",
                      2: "subtraction",
                      3: "multiplication",
                      4: "division"}
        for key, value in operations.items():
            print(f"{key}: {value}")

        while True:
            user_answer_str = input("Please chose the operation, please: ")
            if not user_answer_str:
                print("Please enter something. Try again.")
                continue
            if not user_answer_str.isdigit():
                print("Only numbers! Try again.")
                continue
            else:
                user_answer = int(user_answer_str)
                if user_answer < 1 or user_answer > 4:
                    print("Wrong value. Try again!")
                    continue
                else:
                    if user_answer == 1:
                        self.addition(first_number, second_number)
                        return 0
                    elif user_answer == 2:
                        self.substraction(first_number, second_number)
                        return 0
                    elif user_answer == 3:
                        self.multiplication(first_number, second_number)
                        return 0
                    else:
                        self.division(first_number, second_number)
                        return 0


def main():
    app = calculator()
    app.say_hi()
    while True:
        first_number = app.first_user_number()
        if first_number is None:
            print("Exit the app!")
            break
        second_number = app.second_user_number()
        if second_number is None:
            print("Exit the app!")
            break

        app.chose_operation(first_number, second_number)


if __name__ == "__main__":
    main()
