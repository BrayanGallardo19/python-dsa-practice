class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, cadena: str):
        return sum(ord(c) for c in cadena)

    def add(self, key, value):
        indice = self.hash(key)
        if indice not in self.collection:
            self.collection[indice] = {}
        self.collection[indice][key] = value

    def remove(self, key):
        indice = self.hash(key)
        if indice in self.collection and key in self.collection[indice]:
            del self.collection[indice][key]

    def lookup(self, key):
        indice = self.hash(key)
        if indice in self.collection and key in self.collection[indice]:
            return self.collection[indice][key]
        return None