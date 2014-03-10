def shortest_path(n1, n2, g, distance, d):
    if distance[n1] > d:
        distance[n1] = d
        d += 1
        for e in g:
            if e[0] == n1: 
                shortest_path(e[1], n2, g, distance, d)


def shortpath_queue(n1, n2, g):

    queue = [[n1]]

    while len(queue) > 0:
        # get a path
        p = queue.pop()

        # last node in the path
        n = p[-1]

        # get adjasent 
        for e in g:
            if e[0] == n:
                if e[1] == n2:
                    p.append(n2)
                    return p
                else:
                    np = p[:]
                    np.append(e[1])
                    queue.insert(0, np)
    return []



if __name__ == '__main__':
    g = [[1, 2],
     [1, 4],
     [2, 1],
     [2, 3],
     [2, 5],
     [3, 2],
     [3, 11],
     [4, 1],
     [4, 5],
     [4, 7],
     [5, 2],
     [5, 4],
     [5, 6],
     [5, 8],
     [6, 5],
     [6, 9],
     [6, 10],
     [7, 4],
     [7, 13],
     [8, 5],
     [8, 14],
     [9, 6],
     [9, 12],
     [10, 6],
     [10, 11],
     [11, 3],
     [11, 10],
     [12, 9],
     [13, 7],
     [13, 14],
     [14, 8],
     [14, 13]]

    distance = [float('inf') for i in range(15)]
    n1 = 1
    n2 = 12
    shortest_path(n1, n2, g, distance, 0)

    # print distance
    print shortpath_queue(n1, n2, g)
