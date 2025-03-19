def maxOfThree(a,b,c):
    if b < a > c:
        return f"Najwieksza z trzech liczb to {a}"
    elif a < b > c:
        return f"Najwieksza z trzech liczb to {b}"
    else:
        return f"Najwieksza z trzech liczb to {c}"


print(maxOfThree(10, 4 ,1))