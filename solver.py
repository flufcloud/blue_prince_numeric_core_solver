from operator import add, sub, mul, truediv
from itertools import permutations

sym = {sub: '-', mul: '*', truediv: '/', add: '+'}

def format_answer(answer):
    operands = [
       f"{sym[op]}{num}"
        for op, num in zip(
            answer['operators'], answer['numbers']
        )
    ]
    response = ' '.join(operands) + f" = {int(answer['result'])}"
    return response

def permute(a, b, c, d):
    for second, third, fourth in permutations([sub, mul, truediv], 3):
        try:
            result = fourth(third(second(a, b), c), d)
            yield {
                "result": result,
                "operators": [add, second, third, fourth],
                "numbers": [a, b, c, d],
            }
        except ZeroDivisionError:
            yield {
                "result": -1,
                "operators": [add, second, third, fourth],
                "numbers": [a, b, c, d],
            }

def core(a, b, c, d):
    answers = list(permute(a, b, c, d))
    answers = sorted(answers, key=lambda answer: answer['result'])
    for answer in answers:
        if answer['result'] is None:
            continue
        if answer['result'] < 0:
            continue
        if answer['result'] != round(answer['result']):
            continue
        print(format_answer(answer))
