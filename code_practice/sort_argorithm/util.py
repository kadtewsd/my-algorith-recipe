def create_ord(val: str, len: int) -> int:
    return sum([ord(c.lower()) for c in val[0:len]])

def compare_word(a: str, b: str) -> int:
    min_len = len(min(a, b))
    a_ord = a[0:min_len].lower()
    b_ord = b[0:min_len].lower()
    # print(f"{a_ord == b_ord}")
    if a_ord == b_ord:
        return 0
    elif a_ord < b_ord:
        return 1
    else:
        return -1
