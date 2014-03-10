
def count(n):

    if n < 3:
        return n
    elif n == 3:
        return 4
    else:
        return count(n-1) + count(n-2) + count(n-3)


if __name__ == '__main__':
    for i in range(0, 16):
        print i, count(i)

