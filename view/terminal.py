from parser.arithmetic_exception import ArithmeticException
from parser.parser import calculate_phrase


def run_calculator():
    print("enter your phrase! (enter <end> if you want to terminate program)")
    while True:
        phrase = input()
        if phrase == "end":
            print("shutting down the program!")
            break
        try:
            output = calculate_phrase(phrase)
        except ArithmeticException:
            print("your phrase has some arithmetic or semantic erroneous")
            continue
        print(f"result: {output}")
