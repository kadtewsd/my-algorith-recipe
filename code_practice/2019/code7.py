from typing import List

def calculate(dp: List[List[int]], value: List[str], current_line: int):
    value_index = 0
    for i in range(len(value)):
        print(value[value_index])
        dp[current_line][i] = value[value_index]
        value_index += 1

# N = int(input())
N = 6
# syain = input().splitlines()
syain = [
"10 10 -10 -10 -10",
"10 -10 -10 -10",
"-10 -10 -10",
"10 -10",
"-10",
]
dp = [[0] * (N - 1) for _ in range(N - 2) ]
for i in range(N - 2):
    print(syain[i])
    calculate(
        dp=dp,
        value=syain[i].split(" "),
        current_line=i,
    )


print(dp)


N = int(input())
A = [[0]*N for _ in range(N)]

for i in range(N-1):
    values = list(map(int, input().split()))
    for j, v in enumerate(values):
        A[i][i + j + 1] = v
        A[i + j + 1][i] = v

from itertools import combinations

score = [0] * (1 << N)
for bit in range(1 << N):
    members = [i for i in range(N) if bit & (1 << i)]
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            score[bit] += A[members[i]][members[j]]


dp = [0] * (1 << N)

for bit in range(1 << N):
    sub = bit
    while sub:
        dp[bit] = max(dp[bit], dp[bit ^ sub] + score[sub])
        sub = (sub - 1) & bit  # bitの部分集合を列挙


print(dp[(1 << N) - 1])