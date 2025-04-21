import sys

# Read all 8 input bits (0 or 1), one per line
input_bits = list(map(int, sys.stdin.read().split()))

# Reverse the list to match bit weights (rightmost bit = lowest power)
input_bits.reverse()

# Convert binary to decimal
decimal_value = 0
weight = 1

for bit in input_bits:
    decimal_value += bit * weight
    weight *= 2

print(decimal_value)
