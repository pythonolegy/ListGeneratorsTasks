a = '79-900'
b = '80-155'


def code_list(a, b):
    a = int(a.replace('-', ''))
    b = int(b.replace('-', ''))
    c = []
    while a != b-1:
        a += 1
        c.append(f"{str(a)[:2]}-{str(a)[2:]}")
    print(c)


code_list(a, b)
