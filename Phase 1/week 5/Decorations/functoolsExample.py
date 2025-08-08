# functools.cache example

import functools

@functools.cache
def fibbonacci(n):
    if n < 2:
        return n
    return fibbonacci(n-1) + (fibbonacci(n-2))

print(fibbonacci(40))