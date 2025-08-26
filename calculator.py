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

    def chose_operation(self, first_num, second_num):
        operations = {1: "addition",
                      2: "subtraction",
                      3: "multiplication",
                      4: "division"}
        print("What kind of operation do you want to get? ")
        print(operations)  # Продолжить работу над выборром операции


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
