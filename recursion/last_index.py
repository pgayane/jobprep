def last_index(e, list):

    if list == []:
        return -1

    if list[0] == e:
        index = 0
    else:
        index = -1

    last = last_index(e, list[1:])
    if last != -1:
        return last + 1
    else:
        return index


def last_index_linkedlist(e, linkedlist):
    if linkedlist is None:
        return -1

    if linkedlist[0] == e:
        index = 0
    else:
        index = -1

    last = last_index_linkedlist(e, linkedlist[1])
    if last != -1:
        return last + 1
    else:
        return index

if __name__ == '__main__':
    print last_index(5, [1, 2, 4, 6, 5, 2, 7])
    print last_index(5, [1, 2, 4, 6, 2, 7])
    print last_index(5, [1, 2, 5, 4, 6, 5, 2, 7])

    print last_index_linkedlist(5, [1, [2, [4, [6, [5, [2, [7, None]]]]]]])
