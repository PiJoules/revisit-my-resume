from functools import cmp_to_key


def sort_int_strs(x, y):
    if x == y:
        return 0

    min_len = min(len(x), len(y))
    for i in range(min_len):
        dx = int(x[i])
        dy = int(y[i])
        if dx > dy:
            return 1
        elif dx < dy:
            return -1
        # Equal otherwise

    # Return smaller number first
    if len(x) < len(y):
        return 1
    elif len(y) < len(x):
        return -1
    return 0


def largest_num(lst):
    str_lst = list(map(str, lst))
    sorted_strs = reversed(sorted(str_lst, key=cmp_to_key(sort_int_strs)))
    return int("".join(sorted_strs))


print(largest_num([50, 2, 1, 9, 5, 5]))
print(largest_num([52, 5, 3]))
