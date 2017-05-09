def merge_lists(lst1, lst2):
    if len(lst1) < len(lst2):
        smaller = lst1
        larger = lst2
    else:
        smaller = lst2
        larger = lst1

    result = []
    for i in range(len(smaller)):
        result.append(lst1[i])
        result.append(lst2[i])
    return result + larger[len(smaller):]


lst1 = [1, 2, 3]
lst2 = ["a", "b", "c"]
assert merge_lists(lst2, lst1) == ["a", 1, "b", 2, "c", 3]
assert merge_lists(lst2, [1, 2]) == ["a", 1, "b", 2, "c"]
assert merge_lists(["a", "b"], lst1) == ["a", 1, "b", 2, 3]
