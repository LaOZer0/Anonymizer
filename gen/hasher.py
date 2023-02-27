import hashlib
from .utils import COUNT_WRITE

P = 1000000014000000119


def hashFunction(surname: str, name: str, middleName: str) -> list:
    encodedName = name.encode('utf-8')
    encodedSurname = surname.encode('utf-8')
    encodedMiddleName = middleName.encode('utf-8')

    shaName = hashlib.sha3_512(encodedName)
    shaSurname = hashlib.sha3_512(encodedSurname)
    shaMiddleName = hashlib.sha3_512(encodedMiddleName)

    return [shaSurname.hexdigest(), shaName.hexdigest(), shaMiddleName.hexdigest()]


def HashToInt(hashes: list) -> int:
    return int(hashes[0] + hashes[1] + hashes[2], 16)


class DbHasher:
    def __init__(self, filename: str, delimiter: str = ";", fake_len: int = COUNT_WRITE):
        self.filename = filename
        self.file = open(filename, "r", encoding="utf-8")
        self.delimiter = delimiter
        self.fake_len = fake_len
        self.titles = self.split_row(self.file.readline().rstrip())
        self.row = self.split_row(self.file.readline().rstrip())

    def split_row(self, row: str):
        return row.split(self.delimiter)

    def close(self):
        self.file.close()

    def __iter__(self):
        self.row = self.split_row(self.file.readline().rstrip())
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            return StopIteration
        current_hash = hashFunction(self.row[0], self.row[1], self.row[2])
        result = HashToInt(current_hash) % P % self.fake_len
        self.row = self.split_row(self.file.readline().rstrip())
        return result

    def __str__(self):
        return str(self.row)
