import numpy as np
from typing import Callable

Array_Function = Callable[[np.ndarray], np.ndarray]
Chain = list[Array_Function]


def chain_length_2(chain: Chain, a: np.ndarray) -> np.ndarray:
    '''
    Evaluates two functions in a row, in a "Chain"
    '''

    assert len(chain) == 2
    '''
    Length of input "chain" should be 2
    '''

    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(a))

# Kita buat dua fungsi sederhana


def tambah_sepuluh(x: np.ndarray) -> np.ndarray:
    return x + 10


def kali_dua(x: np.ndarray) -> np.ndarray:
    return x * 2


my_chain = [tambah_sepuluh, kali_dua]

# Input data
x_input = np.array([1, 2, 3])


# Proses: (1 + 10) * 2 = 22
hasil = chain_length_2(my_chain, x_input)

print(hasil)  # Output: [22, 24, 26]
