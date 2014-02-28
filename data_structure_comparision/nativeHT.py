class NaiveHT:

    def __init__(self):
        self.hash_table = {}

    def put(self, key, value):
        self.hash_table[key] = value

    def get(self, key):
        return self.hash_table[key]

    def __str__(self):
        return str(self.hash_table)

    def __repr__(self):
        return self.__str__()