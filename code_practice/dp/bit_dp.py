# N = int(input())
from typing import List

# syain = input().splitlines()
# メンバー数が 6 の場合、入力される行数は 6 - 1 = 5 行になる。
# なぜなら、入力は「i < j を満たすペア (i, j) に対する幸福度」が与えられており、
# 最終行は (4, 5) の1組で終了する。
# よって、データ読み込み時のループは range(6 - 1) が正しい。

# ただし、後続のスコア計算では、メンバーの任意のペア (i, j) にアクセスするため、
# たとえば (5, 1) のように i > j となるケースも発生する。
# このとき、未初期化だと IndexError や不正なデータ参照につながる。

# したがって、幸福度を格納する二次元配列は、入力行数ではなく、
# メンバー数 N を用いた N × N 配列として初期化する必要がある。
syain = [
    "10 10 -10 -10 -10", #f0,1,f0,2,f0,3
    "10 -10 -10 -10", #f1,1,#f1,2,#f1,3,
    "-10 -10 -10", #f2,1,f2,2
    "10 -10", #f3,1
    "-10", #f4,1
]

M = 6
L = M - 1
#行数は 5 であるが、後続の処理でメンバーの数だけインデックスアクセスする必要がある。
#この際に、行数で初期化してしまうと、メンバーの数が行数を上まった際に例外が発生してしまう。
# 例 : 5 0。5,0 という 物に対応するために、L (= 行数) ではなく、M (メンバー数) でデータを構築する。
# 結構落とし穴
data = [[0] * M for _ in range(M)]
# data = [[0] * L for _ in range(L)]
# print(data)

for i in range(L):
    value = list(map(int, syain[i].split()))
    # print(value)
    for j, v in enumerate(value):
        # print(j)
        #i =1 の場合は、J は、2, 3, 4, 5。
        #つまり、j は 常に、i に対して + 1 の関係性を持つ必要がある。
        # value で enumerate しているので、6 (添え字 5) はこない。
        data[i][i + j + 1] = v
        data[i + j + 1][i] = v

# print(data[5][0])

# 組み合わせに対しての点数を構築する。0,1 は 10 といったようなデータ
# カラ集合を含めたすべての組み合わせに対しての点数を構築するために、score として構築
score = [0] * (1 << M)
# print(len(score))
for bit in range(1 << M):
    # 人数 M に対して M 個ビットずらし。bit を左にずらすと、10 進数の値が 2 乗されていく。
    # これが、選ぶ・選ばないの二通りに対しての乗数とマッチする。
    # たとえば、bit = 3 である場合、
    # 011 になる。0, 1 が選択されている状態になっている
    # これに対して、j が増えていく際に、
    # j = 0 = 0-> 00000 => MISS!
    # j = 1 = 1 => 00001 => HIT!
    # j = 2 = 2 => 00010 => HIT!
    # J = 3 = 4 => 00100 => HIT!
    # J = 4 = 16 => 01000 => MISS!
    # J = 5 = 32 => 10000 => MISS!
    members = [j for j in range(M) if bit & (1 << j)]
    # print(f"{bit} {members}")
    #member のすべての組み合わせで combination を構築する
    for i in range(len(members)):
        # いつ関係性としては fi12, f23 になるので、常に i + 1 が開始のループになる
        # このため、0,1 といった組み合わせになっていないものは除外される
        for j in range(i + 1, len(members)):
            # print(f"members {members[i]} {members[j]}")
            # print(f"{bit} {i} {j}")
            # print(f"{bit} {i} {j} {data[members[i]][members[j]]}")
            #メンバーに割り当てられている番号が、初期化にしたデータの番号に該当している
            # 例えば、f0,1
            score[bit] += data[members[i]][members[j]]

print(score)

# sub = M
# while sub: