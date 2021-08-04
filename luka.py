


def digital_root(n):
    b=str(n)
    k = 0
    for i in range(len(b)):
        k += int(b[i])
    if k < 10:
        return k
    while k > 9:
        s=k
        l=str(s)
        f=0
        for j in range(len(l)):
            f+=int(l[j])
        k=f
    return k


print(digital_root(16))