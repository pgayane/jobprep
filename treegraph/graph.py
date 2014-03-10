
def find_path(n1, n2, g, visited):
    if n1 == n2:
        return [n1]
    else:
        p = []
        for n in g[n1]:
            if n not in visited:
                visited.append(n)
                r = find_path(n, n2, g, visited)
                if r != []:
                    p.append(n1)
                    p.extend(r)
                    break
        return p





if __name__ == '__main__':
    g = [[],
     [2, 4],
     [1, 3, 5],
     [2],
     [1, 7],
     [2, 6, 8],
     [5, 9, 10],
     [4],
     [5],
     [6, 12],
     [6, 11],
     [10],
     [9]]

     
    print find_path(1, 10, g, [])