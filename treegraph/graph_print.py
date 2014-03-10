class Stack:

    def __init__(self):
        self.data = []

    def get(self):
        return self.data.pop()

    def put(self, element):
        self.data.append(element)

    def count(self):
        return len(self.data)



class Queue:

    def __init__(self):
        self.data = []

    def get(self):
        return self.data.pop()

    def put(self, element):
        self.data.insert(0, element)

    def count(self):
        return len(self.data)


def print_graph(g, storage):

    store = storage()
    store.put(1)
    visited = [1]

    while store.count() > 0:
        current_node = store.get()
        print current_node

        for neighbor in g[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                store.put(neighbor)



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

    print 'printing with queue'
    print_graph(g, Queue)

    print 'printing with stack'
    print_graph(g, Stack)