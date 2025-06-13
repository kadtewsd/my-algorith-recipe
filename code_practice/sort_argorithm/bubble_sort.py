from util import compare_word

input = ["ZGrad", "gorilla", "duce", "kiss", "apple", "Foreigner"]

for i in range(0, len(input)):
    # i がソート済みであるのでループ不要。また、隣接の比較をするので、-1 してすべてのループを回さない
    for j in range(1, len(input) - i):
        current = input[j - 1]
        compare = input[j]
        # print(f"j {j} {current} {compare}")
        #比較元よりも比較先の方が大きな数であったら
        compare_result =  compare_word(current, compare)
        # print(compare_result)
        if compare_result == -1:
            input[j]= current
            input[j - 1] = compare
            # print(f"j {j} {input}")

print(input)


