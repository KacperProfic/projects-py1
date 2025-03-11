


def createFib():
    fib = int(input("how many fibonacci numbers do you want to generate: "))
    i = 1
    if fib == 0:
        res = []
    elif fib == 1:
        res = [1]
    elif fib == 2:
        res = [1, 1]
    elif fib > 2:
        res = [1, 1]
        while i < (fib - 1):
            res.append(res[i] + res[i-1])
            i += 1
    return res
print(createFib())
input()