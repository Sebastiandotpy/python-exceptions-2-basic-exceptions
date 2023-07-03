from typing import Tuple


class MathematicalError(Exception):
    pass


def parse_input(user_input: str) -> Tuple[float, str, float]:
    elements = user_input.split()

    if len(elements) != 3:
        raise MathematicalError('Input does not consist of three elements')

    try:
        n1 = float(elements[0])
        op = elements[1]
        n2 = float(elements[2])
    except ValueError:
        raise MathematicalError('The first and third input value must be numbers')

    valid_operators = ['+', '-', '/', '*']
    if op not in valid_operators:
        raise MathematicalError('Invalid operator. Can only use "+" or "-"')
    return n1, op, n2

def calculate(n1: float, op: str, n2: float) -> float:
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '/':
        return n1 / n2
    if op == '*':
        return n1 * n2

if __name__ == '__main__':
    while True:
        user_input = input('>>> ')
        if user_input == 'quit':
            break

        try:
            n1, op, n2 = parse_input(user_input)
            result = calculate(n1, op, n2)
            print(result)
        except MathematicalError as e:
            print(f'Error: {str(e)}')
