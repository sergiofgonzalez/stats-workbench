from math import isnan, sqrt
from cs03_stack import Stack


def is_number(str):
    try:
        str_as_int = int(str)
        return True
    except ValueError:
        try:
            str_as_float = float(str)
            return True
        except ValueError:
            return False


class StackCalculator(Stack):

    def __init__(self):
        super().__init__()

    def enter(self, user_input):
        try:
            user_input_as_int = int(user_input)
            self.push(user_input_as_int)
        except ValueError:
            try:
                user_input_as_float = float(user_input)
                self.push(user_input_as_float)
            except ValueError:
                self.push(user_input)

    def add(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op1 + op2)

    def add(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op1 + op2)

    def sub(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op1 - op2)

    def mult(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op1 * op2)

    def div(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op1 / op2)

    def neg(self):
        op = self.pop()
        self.push(-op)

    def sqrt(self):
        op = self.pop()
        self.push(sqrt(op))

    def pow(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op1 ** op2)

    def mod(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op1 % op2)

    def swap(self):
        op2 = self.pop()
        op1 = self.pop()
        self.push(op2)
        self.push(op1)


stack_calculator = StackCalculator()


def processUserInput(user_input):
    if user_input == "+":
        stack_calculator.add()
    elif user_input == "-":
        stack_calculator.sub()
    elif user_input == "*":
        stack_calculator.mult()
    elif user_input == "/":
        stack_calculator.div()
    elif user_input == "neg":
        stack_calculator.neg()
    elif user_input == "sqrt":
        stack_calculator.sqrt()
    elif user_input == "mod":
        stack_calculator.mod()
    elif user_input == "swap":
        stack_calculator.swap()
    elif user_input == "pow":
        stack_calculator.pow()
    else:
        stack_calculator.enter(user_input)


print("== Stack based calculator ==")

user_input = input("? ")
while user_input.lower() != "quit":
    processUserInput(user_input)
    print(stack_calculator)
    user_input = input("? ")

print("\nquit signal received")
