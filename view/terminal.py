from parse.arithmetic_exception import ArithmeticException
from parse.parser import get_value_phrase


def run_calculator():
    while True:
        print("enter your phrase! (enter <end> if you want to terminate program)")
        phrase = input()
        if phrase == "end":
            print("shutting down the program!")
            break
        try:
            output = get_value_phrase(phrase)
        except ArithmeticException:
            print("your phrase has some arithmetic or semantic erroneous")
            continue
        print(f"result: {output}")
