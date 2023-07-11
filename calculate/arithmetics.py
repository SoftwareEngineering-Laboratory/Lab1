def multiply(x: float, y: float) -> float:
    return x * y


def division(x: float, y: float) -> float:
    return x / y


def difference(x: float, y: float) -> float:
    return x - y


def summation(x: float, y: float) -> float:
    return x + y


def get_function(operator: str):
    operator_to_function = {
        '*': multiply,
        '/': division,
        '-': difference,
        '+': summation,
    }
    return operator_to_function[operator]
