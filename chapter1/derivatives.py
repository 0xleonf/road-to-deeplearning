from typing import Callable
import numpy as np


def equation(x: np.ndarray) -> np.ndarray:
    return x ** 2


def deriv(func: Callable[[np.ndarray], np.ndarray], input_: np.ndarray, delta: float = 0.001) -> np.ndarray:
    '''
    Evaluates the derivative of a function "func" at every element in the "input_" array
    '''
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)


input_ = np.array([3.0])
result = deriv(equation, input_)

print(f'derivatives at {input_} x^2 : {result}')
