import numpy as np
from numpy import ndarray
from typing import Callable

Array_Function = Callable[[ndarray], ndarray]
Chain = list[Array_Function]


def deriv(func: Callable[[ndarray], np.ndarray], input_: ndarray, delta: float = 0.001) -> ndarray:
    '''
    Evaluates the derivative of a function "func" at every element in the "input_" array
    '''
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)


def chain_deriv_2(chain: Chain,
                  input_range: ndarray) -> ndarray:
    '''
    Uses the chain rule to compute the derivative of two nested functions:
    (f2(f1(x))' = f2'(f1(x)) * f1'(x)
    '''
    assert len(chain) == 2, \
        "This function requires 'Chain' objects of length 2"

    assert input_range.ndim == 1, \
        "Function requires a 1 dimensional ndarray as input_range"

    f1 = chain[0]
    f2 = chain[1]
    # df1/dx
    f1_of_x = f1(input_range)
    # df1/du
    df1dx = deriv(f1, input_range)
    # df2/du(f1(x))
    df2du = deriv(f2, f1(input_range))
    # Multiplying these quantities together at each point
    return df1dx * df2du
