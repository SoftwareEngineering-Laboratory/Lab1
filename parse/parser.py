from calculate.arithmetics import get_function
from parser.arithmetic_exception import ArithmeticException
from parser.phrase import Phrase, Leaf, Composite


def convert_numbers_to_leaf(phrase):
    converted_phrase = []
    i = 0
    digit = ""
    while i < len(phrase):
        if phrase[i].isdigit():
            j = i
            while j < len(phrase) and phrase[j].isdigit():
                digit += phrase[j]
                j += 1
            i = j
            leaf = Leaf(float(digit))
            digit = ""
            converted_phrase.append(leaf)
        else:
            converted_phrase.append(phrase[i])
        i += 1
    return converted_phrase


def break_operand(operand):
    if '*' in operand and '/' in operand:
        index_mul = operand.index('*')
        index_div = operand.index('/')
        if index_mul < index_div:
            left_operand = operand[:index_mul]
            right_operand = operand[index_mul + 1:]
            operator = get_function('*')
        else:
            left_operand = operand[:index_div]
            right_operand = operand[index_div + 1:]
            operator = get_function('/')
    elif '*' in operand:
        index_mul = operand.index('*')
        left_operand = operand[:index_mul]
        right_operand = operand[index_mul + 1:]
        operator = get_function('*')
    elif '/' in operand:
        index_div = operand.index('/')
        left_operand = operand[:index_div]
        right_operand = operand[index_div + 1:]
        operator = get_function('/')
    elif '-' in operand and '+' in operand:
        index_sum = operand.index('+')
        index_dif = operand.index('-')
        if index_sum < index_dif:
            left_operand = operand[:index_sum]
            right_operand = operand[index_sum + 1:]
            operator = get_function('+')
        else:
            left_operand = operand[:index_dif]
            right_operand = operand[index_dif + 1:]
            operator = get_function('-')
    elif '-' in operand:
        index_dif = operand.index('-')
        left_operand = operand[:index_dif]
        right_operand = operand[index_dif + 1:]
        operator = get_function('-')
    else:
        index_sum = operand.index('+')
        left_operand = operand[:index_sum]
        right_operand = operand[index_sum + 1:]
        operator = get_function('+')
    return Composite(convert_to_phrase(left_operand), convert_to_phrase(right_operand), operator)


def convert_to_phrase(operand):
    if len(operand) == 1:
        return operand[0]
    elif len(operand) == 2:
        if operand[0] == '+':
            return operand[1]
        elif operand[0] == '-':
            left_phrase = Leaf(-1)
            right_phrase = operand[1]
            operand = get_function('*')
            return Composite(left_phrase, right_phrase, operand)
        else:
            raise ArithmeticException()
    else:
        return break_operand(operand)


def remove_inner_parentheses(phrase):
    i = 0
    start_index = -1
    end_index = -1
    while i < len(phrase):
        if phrase[i] == "(":
            start_index = i
        elif phrase[i] == ")":
            end_index = i
            break
        i += 1
    return phrase[:i] + [convert_to_phrase(phrase[start_index + 1:end_index])] + phrase[end_index:]


def generate_phrase_tree(phrase: str) -> Phrase:
    phrase_of_leafs = ["("] + convert_numbers_to_leaf(list(phrase)) + [")"]
    while "(" in phrase_of_leafs:
        phrase_of_leafs = remove_inner_parentheses(phrase_of_leafs)
    final_phrase = convert_to_phrase(phrase_of_leafs)
    return final_phrase


def get_value_phrase(input_phrase: str) -> float:
    phrase: Phrase = generate_phrase_tree(input_phrase)
    return phrase.get_value()
