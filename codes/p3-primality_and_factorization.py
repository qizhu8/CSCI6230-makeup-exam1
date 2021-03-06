#!/usr/bin/env python3
import numpy as np
import Number_Package as npkg


candidate_numbers = [31531, 520482, 485827, 15485863]
prime_flag = [False] * len(candidate_numbers)

n = candidate_numbers[0]
check_round = 100
for idx, n in enumerate(candidate_numbers):
    is_prime = npkg.miller_rabin_primality_check(n, check_round)
    if is_prime:
        print("{idx}: number {n} is prime".format(idx=idx, n=n))
        prime_flag[idx] = True
    else:
        print("{idx}: number {n} is composite".format(idx=idx, n=n))
        factors = npkg.factorize(n)
        factors.sort()
        # print
        factors_str = str(n) + "=" + str(factors[0])
        for f in factors[1:]:
            factors_str += " * " + str(f)
        print(factors_str)
