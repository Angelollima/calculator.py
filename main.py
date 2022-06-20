import os
from math import sqrt

BOLD_TEXT = "\033[1m{:^60}\033[0m"

OPTIONS = """options:
+ for addition
- for subtraction
* for multiplication
/ for division
s for square root
c for clean
q to exit
:-> """


operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y > 0 else "Can't divide by zero",
    "s": lambda x: sqrt(x),
}


def main() -> None:
    print(BOLD_TEXT.format("Welcome to Easy Calculator"))

    while True:
        operation = input(OPTIONS)
        if operation == "q":
            print(BOLD_TEXT.format("Cya... hope to see you soon!"))
            exit()

        elif operation == "c":
            os.system("clear" if os.name == "posix" else "cls")

        elif operation == "s":
            number = input("Enter one number: ")
            if not number.isnumeric():
                print(BOLD_TEXT.format("That's not a number!"))
                continue
            r = operations["s"](float(number))
            print(BOLD_TEXT.format(f"The square of {number} is: {r:.2f}"))

        elif operation in operations:
            number_1 = input("Enter first number: ")
            number_2 = input("Enter second number: ")
            if not number_1.isnumeric() or not number_2.isnumeric():
                print(BOLD_TEXT.format("Both values needs to be of numeric type!"))
                continue
            r = operations[operation](float(number_1), float(number_2))
            print(BOLD_TEXT.format(f"{number_1} {operation} {number_2} = {r}"))

        else:
            print(BOLD_TEXT.format(f"Hmm.. '{operation}' that's not an operation!"))


if __name__ == "__main__":
    main()
