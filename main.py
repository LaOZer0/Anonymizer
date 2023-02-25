import csv
from generators import generate_fake_db
from hasher import COUNT_WRITE, DbHasher



def Anonymize(path: str):
    print(next(hasher))
    next(hasher)
    print(hasher)
    print("penis")
    next(hasher)
    print(hasher)
    with open(path, encoding="utf-8", mode='r') as original_db:

            with open(path, encoding='utf-8', mode='w') as new_original_db:
                new_original_db_writer = csv.writer(new_original_db, delimiter=';', lineterminator="\r")
                fake_db_list = list(fake_db)
                new_original_db_writer.writerow(first_line)
                for i in range(len(hashes)):
                    new_original_db_writer.writerow(fake_db_list[hashes[i] - 1].split(';'))
    return 0

if __name__ == "__main__":
    generate_fake_db("gen.csv")
