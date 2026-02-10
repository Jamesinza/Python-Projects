class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, x):
        return sum(ord(i) for i in x)

    def add(self, x, y):
        hashed_x = self.hash(x)
        if hashed_x not in self.collection:
            self.collection[hashed_x] = {}
        self.collection[hashed_x][x] = y

    def remove(self, x):
        hashed_x = self.hash(x)
        if hashed_x in self.collection and x in self.collection[hashed_x]:
            del self.collection[hashed_x][x]
            if not self.collection[hashed_x]:
                del self.collection[hashed_x]

    def lookup(self, x):
        hashed_x = self.hash(x)
        if hashed_x in self.collection and x in self.collection[hashed_x]:
            return self.collection[hashed_x][x]
        return None
