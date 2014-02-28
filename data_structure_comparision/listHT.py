class listHT:

    def __init__(self):
        self.list=[]

    def put(self, key, value):
        self.list.append((key, value))

    def get(self, key):
        for pair in self.list:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        for pair in self.list:
            if pair[0] == key:
                self.list.remove(pair)
                return True
        return False

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        return self.__str__()