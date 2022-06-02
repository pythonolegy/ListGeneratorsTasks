x = input().split()
newlist = [int(x) for x in x]
a = []


def list_generator():
    for elem in range(min(newlist), max(newlist) + 1):
        b = []
        if elem in newlist:
            a.append(elem)
        if elem not in newlist:
            b.append(elem)
            if elem != []:
                a.append(b)


print(a)
