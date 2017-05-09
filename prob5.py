class Add:
    pass

class Sub:
    pass

class Join:
    pass


from itertools import product
from prob2 import merge_lists


def merge_joins(stack):
    assert len(stack) == 17, len(stack)
    joined_stack = []
    i = 0
    while i < len(stack):
        if stack[i] == Join:
            last = joined_stack.pop()
            last = last*10 + stack[i+1]
            joined_stack.append(last)
            i += 2
        else:
            joined_stack.append(stack[i])
            i += 1
    return joined_stack


def run_stack(stack):
    joined_stack = merge_joins(stack)

    # Go through all joins
    s = joined_stack[0]
    for i in range(1, len(joined_stack), 2):
        instr = joined_stack[i]
        arg = joined_stack[i+1]
        if instr == Add:
            s += arg
        elif instr == Sub:
            s -= arg
        else:
            raise RuntimeError("Unknown insrtuction {}".format(instr))

    return s


def stack_str(stack):
    stack = merge_joins(stack)

    line = []
    for elem in stack:
        if isinstance(elem, int):
            line.append(str(elem))
        elif elem == Add:
            line.append("+")
        elif elem == Sub:
            line.append("-")
        else:
            raise RuntimeError("Unknown element {}".format(elem))

    return " ".join(line)



def always_100():
    instr_combos = product([Add, Sub, Join], repeat=8)
    nums = list(range(1, 10))
    working = []
    for combo in instr_combos:
        stack = merge_lists(nums, list(combo))
        if run_stack(stack) == 100:
            working.append(stack)
    return working

results = always_100()
print("{} solutions".format(len(results)))
print("----------------")
for result in results:
    print(stack_str(result))


