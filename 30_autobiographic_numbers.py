# given a number it is considered autobiographic if count of the index matches the value at the index.


def FindAutoCount(n):
    for i in range(len(n)):
        val = str(i)
        tam = int(n[i])
        cnt = n.count(val)
        if cnt==tam:
            return len(n)-n.count("0")
        else:
            return 0


print(FindAutoCount(input()))
