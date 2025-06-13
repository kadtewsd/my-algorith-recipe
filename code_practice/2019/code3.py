import sys

input = sys.stdin.read().split(" ")
sort = sorted([int(i) for i in input], reverse=True)
print(sort[2])