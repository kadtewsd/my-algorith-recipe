import sys
from typing import Set, List

# first_line = "6 7".split(" ")
first_line = input().split(" ")
user_number = int(first_line[0])
log_line = int(first_line[1])

# ユーザーの番号 1 ~ N (N + 1 にしないと N にならない)
user_numbers = range(1, user_number + 1)
# ログの行
logs = sys.stdin.read().splitlines()
# logs = [
# "1 1 2",
# "1 2 3",
# "1 3 4",
# "1 1 5",
# "1 5 6",
# "3 1",
# "2 6",
# ]

# フォロー状況記憶マップ
follow_map_set = {}
for user in user_numbers:
    follow_map_set.setdefault(user, set())

follow_map_list = {}
for user in user_numbers:
    follow_map_list.setdefault(user, list())

for log in logs:
    contents = list(map(int, log.split(" ")))
    operation = contents[0]
    operation_user = contents[1]
    operation_user_follow: Set[int] = follow_map_set[operation_user]
    operation_user_follow_list: List[int] = follow_map_list[operation_user]
    # シンプルフォロー
    if operation == 1:
        follow_user =  contents[2]
        operation_user_follow.add(follow_user)
        operation_user_follow_list.append(follow_user)
    elif operation == 2:
        #フォロー全返し
        for user, follow_set in follow_map_set.items():
            if operation_user == user:
                # 自分自身のフォローはないが走査自体はいらないようにする
                continue
            if operation_user in follow_set:
                # フォローされているのであればフォロー返し
                operation_user_follow.add(user)
                operation_user_follow_list.append(user)
    else:
        # フォローフォロー まず自分がフォローしているユーザーを列挙する
        follow_list_count = len(operation_user_follow_list)
        for index in range(0, follow_list_count):
            # follow_set には自分がフォローしているユーザーのリストが入っている。
            # 自分がフォローしているユーザーを取得
            # my_follow: List[int] = follow_map_list[index]
            follow_user = operation_user_follow_list[index]
            # 自分がフォローしているユーザーのフォローユーザーリストを取得
            follow_set: Set[int] = follow_map_set[follow_user]

            for follow_follow in follow_set:
                operation_user_follow.add(follow_follow)
                operation_user_follow_list.append(follow_follow)

# 自分自身がフォローしているユーザーを出していく
for my_follow_user, follows in follow_map_list.items():
    results = ""
    for user in user_numbers:
        if user in follows:
            results += "Y"
        else:
            results += "N"
    print(results)