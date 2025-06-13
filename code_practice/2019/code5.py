from typing import Set, List

def execute_log(follow_map_set: List[Set[int]], log: str):
    contents = list(map(int, log.split(" ")))
    operation = contents[0]
    operation_user = contents[1]
    operation_user_follow: Set[int] = follow_map_set[operation_user]
    # シンプルフォロー
    if operation == 1:
        operation_user_follow.add(contents[2])
    elif operation == 2:
        # フォロー全返し
        for user in range(1, user_number + 1):
            if operation_user == user:
                # 自分自身のフォローはないが走査自体はいらないようにする
                continue
            if operation_user in follow_map_set[user]:
                # 自分をフォローしていたらフォローに追加
                operation_user_follow.add(user)
    else:
        # set が増えてしまうのでループの最後に増やすようにする
        my_follow = set()
        # フォローフォロー まず自分がフォローしているユーザーを列挙する
        for index in operation_user_follow:
            # フォローしているユーザーのフォローを確認
            for follow_follow in follow_map_set[index]:
                if operation_user != follow_follow:
                    my_follow.add(follow_follow)
        operation_user_follow.update(my_follow)


user_number, log_line = map(int, input().split(" "))
# user_number, log_line = 6, 7
# ユーザーの番号 1 ~ N (N + 1 にしないと N にならない)
follow_map_set = [set() for _ in range(user_number + 1)]
# execute_log(follow_map_set, "1 1 2")
# execute_log(follow_map_set, "1 2 3")
# execute_log(follow_map_set, "1 3 4")
# execute_log(follow_map_set, "1 1 5")
# execute_log(follow_map_set, "1 5 6")
# execute_log(follow_map_set, "3 1")
# execute_log(follow_map_set, "2 6")
for _ in range(log_line):
    execute_log(follow_map_set, input())

# 自分自身がフォローしているユーザーを出していく
for i in range(1, user_number + 1):
    results = ""
    for j in range(1, user_number + 1):
        # 自分自身のフォローに該当ユーザーがいるのかを確認
        if j in follow_map_set[i]:
            results += "Y"
        else:
            results += "N"
    print(results)
