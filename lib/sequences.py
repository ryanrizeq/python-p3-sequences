#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    i = 0
    j = 0
    while i < length:
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[j] + sequence[j + 1])
            j += 1
        i += 1
    print(sequence)