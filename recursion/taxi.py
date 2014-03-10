def path_count(nr, nd, n):

    if nr == n or nd == n:
        return 1
    else:
        return path_count(nr+1, nd, n) + path_count(nr, nd+1, n)

if __name__ == '__main__':
    print path_count(0, 0, 2)
