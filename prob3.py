def fib_list(n):
    if n <= 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        result = fib_list(n-1)
        result.append(result[-1] + result[-2])
        return result


assert fib_list(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fib_list(100))
