from typing import List


def sort(result: List[str], first_index: int, s: str) -> int:
    #先頭一文字をヒット
    word = s[first_index]
    #検索対象のインデックス
    search_index = first_index + 1
    next_search_index = None
    for index in range(search_index, len(s)):
        if s[index].isupper():
            result.append(word + s[index])
            #次の大文字のインデックス
            next_search_index = index + 1
            break
        word += s[index]

    return next_search_index

s = input()
# s = "FisHDoGCaTAAAaAAbCAC"

continue_loop = True
first_index = 0
string_length = len(s)
result = []
while continue_loop:
    #次のindex。長さ 4 の AAAAであれば、
    #1度目は、2, 二度目は、4
    # 9 文字の、DoGDoGCaT であれば、
    # 1 度目、3
    # 2　度目 6
    first_index = sort(
        result = result,
        first_index=first_index,
         s = s,
     )
    if string_length <= first_index or first_index is None:
        continue_loop = False

complete = sorted(result)
complete = sorted(result, key=lambda x:x.lower())
sorted_values = "".join(complete)
print(sorted_values)