import sys

# input = [6,1,5,6,3,2,6]
input = sys.stdin.read().splitlines()
size = int(input[0])

#  [] にすると線形検索して仕事量が O(N) になる。しかし。set だと O(1) になる
# seen = []
seen = set()

duplicated = None
# 1..N までの range。重複がないのでここから妥当性を考える
# range の max は未満。要素数が、6 個あるので、6 未満になるため、+ 1 する必要がある
# kotlin の map と異なり、python の map はイテレータを返す。このため、list でラップして何度でもアクセスできるようにしてあげる
data_range = list(map(int, input[1:size + 1]))
for number in data_range:
    # 現在の値が重複に含まれているかの確認
    if number in seen:
        # 重複があったら重複値 (y) をセット
        duplicated = f"{number}"
        break
    seen.add(number)

# 今度は脱落した値が何で合ったかを考える
number_range = set(range(1, size + 1))
# 重複込みのデータに対して、set をかけることで差分を出します
diff = number_range - set(data_range)

if duplicated is None:
    print("Correct")
else:
    # set ではインデックスアクセスできない。list を使ってインデックスアクセスする
    print(f"{duplicated} {list(diff)[0]}")
