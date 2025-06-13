
import sys

input = sys.stdin.read().splitlines()[1:]
current_price = None
previous_price = None
for i in range(len(input)):
    current_price = int(input[i])
    if i == 0:
        previous_price = int(input[i])
        continue
    print_word = None
    if current_price == previous_price:
        print_word = "stay"
    if current_price < previous_price:
        print_word = f"down {previous_price - current_price}"
    if previous_price < current_price:
        print_word = f"up {current_price - previous_price}"
    previous_price = current_price
    print(print_word)