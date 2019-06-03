

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]

    def assign(self, key, value):
        pass

    def retrieve(self, argument):
        pass

    @staticmethod
    def hash(key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size
