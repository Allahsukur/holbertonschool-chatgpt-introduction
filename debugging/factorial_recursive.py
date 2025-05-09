#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Parametrin düzgün daxil edildiyini yoxlayırıq
if len(sys.argv) != 2:
    print("Usage: python factorial.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Please enter a non-negative integer.")
        sys.exit(1)
    f = factorial(number)
    print(f)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    sys.exit(1)
