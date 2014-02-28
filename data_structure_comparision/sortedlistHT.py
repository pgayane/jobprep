class sortedlistHT:

    def __init__(self):
        self.list = []
        self.sorted = False

    def put(self, key, value):
        self.list.append((key, value))
        self.sorted = False

    def get(self, key):
        if not self.sorted:
            self.list.sort()
            self.sorted = True
        index = self.binary_search(key, 0, len(self.list) -1)
        
        if index is None:
            return None
        else:
            return self.list[index][0]


    def remove(self, key):
        
        if not self.sorted:
            self.list.sort()
            self.sorted = True
        
        index = self.binary_search(key, 0, len(self.list)-1)

        if index is None:
            return False
        else:
            del self.list[index]
            return True


    def binary_search(self, key, start, end):
        mid = (start + end) // 2
        if start == end:
            if self.list[start][0] == key:
                return start
            else:
                return None
        else:
            if self.list[mid][0] >= key:
                return self.binary_search(key, start, mid)
            else:
                return self.binary_search(key, mid+1, end)

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        return self.__str__()