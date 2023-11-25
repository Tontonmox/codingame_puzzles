import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
alphabet = string.ascii_lowercase

n = int(input())
matrix = []
start_points = []

for i in range(n):
    matrix.append(input())
    start_points + [j for j,c in enumerate(matrix[i]) if c == 'a']

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(start_points)
