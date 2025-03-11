names = ["Michele", "Robin", "Sara", "Michele"]


def RemoveDuplicates(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return(result)

print(RemoveDuplicates(names))


def RemoveDuplicatesWithSet(arr):
    return list(set(arr))

print(RemoveDuplicatesWithSet(names))