# For initial population generation
# Input Arguments :
# 1. The X_high & X_low matrices
# 2. Population Size

# Return Value: X_init (Initial population matrix)


import random


def initialize(X_hi, X_lo, pop_size):
    X_init = [[0 for x in range(len(X_hi))] for y in range(pop_size)]
    for i in range(0, pop_size, 1):
        for j in range(0, len(X_hi), 1):
            rn = random.uniform(0, 1)
            X_init[i][j] = round(X_lo[j] + rn * (X_hi[j] - X_lo[j]), 4)

    return X_init
