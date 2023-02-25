import GenerateSNILS
import GenerateName
import GenerateBirtday
import csv
import hashlib


def hashFunction (surname: str, name: str, middleName: str) -> list:
    encodedName = name.encode('utf-8')
    encodedSurname = surname.encode('utf-8')
    encodedMiddleName = middleName.encode('utf-8')

    shaName = hashlib.sha3_512(encodedName)
    shaSurname = hashlib.sha3_512(encodedSurname)
    shaMiddleName = hashlib.sha3_512(encodedMiddleName)

    return [shaSurname.hexdigest(), shaName.hexdigest(), shaMiddleName.hexdigest()]


def HashToInt(hashes: list) -> int:
    return int(hashes[0] + hashes[1] + hashes[2], 16)

COUNT_WRITE = 1000
P = 1000000014000000119 


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



def Anonymize(path: str):
    hasher = DbHasher(path)
    next(hasher)
    print(hasher)
    next(hasher)
    print(hasher)
    print("penis")
    next(hasher)
    print(hasher)
    with open(path, encoding="utf-8", mode='r') as original_db:
        original_db_reader = csv.reader(original_db, delimiter=';')
        count = 0
        for _ in original_db_reader:
            count += 1
        len_fake_db = min(10, count * 3)
        hashes = []
        flag = 0
        for row in original_db_reader:
            if flag == 0:
                flag += 1
            else:
                s_name = row[0].split()[0]
                f_name = row[0].split()[1]
                m_name = row[0].split()[2]
                hashes.append(
                        HashToInt(hashFunction(s_name, f_name, m_name))
                        % 1000000014000000119 % len_fake_db
                        )
        with open('fake_db.csv', encoding='utf-8', mode='w') as fake_db:
            fake_db_writer = csv.writer(fake_db, delimiter=';', lineterminator="\n")
            already_write_in_fake_db = 0
            while len_fake_db - already_write_in_fake_db != 0:
                count_write = min(10, len_fake_db - already_write_in_fake_db)
                list_names = GenerateName.GenerateName(count_write)
                list_SNIlS = GenerateSNILS.GenerateListSNILS(count_write)
                list_birthday = GenerateBirtday.GenerateBirthday(count_write)
                help_list = []
                for i in range(count_write):
                    help_list.append(list_names[i][2])
                    help_list.append(list_names[i][0])
                    help_list.append(list_names[i][1])
                    help_list.append(list_SNIlS[i])
                    help_list.append(list_birthday[i])
                    print(help_list)
                    fake_db_writer.writerow(help_list)
                    help_list.clear()
                already_write_in_fake_db += count_write

            first_line = list(original_db)[0].split(';')

            with open(path, encoding='utf-8', mode='w') as new_original_db:
                new_original_db_writer = csv.writer(new_original_db, delimiter=';', lineterminator="\r")
                fake_db_list = list(fake_db)
                new_original_db_writer.writerow(first_line)
                for i in range(len(hashes)):
                    new_original_db_writer.writerow(fake_db_list[hashes[i] - 1].split(';'))
    return 0

def genrateInput():
    len_fake_db = 10000
    fake_db = open('original_db.csv', encoding='utf-8', mode='w')
    fake_db_writer = csv.writer(fake_db, delimiter=';', lineterminator="\n")
    fake_db_writer.writerow(['ФИО', 'Пол', 'Дата рождения', 'СНИЛС'])
    already_write_in_fake_db = 0
    while len_fake_db - already_write_in_fake_db != 0:
        count_write = min(1000, len_fake_db - already_write_in_fake_db)
        list_names = GenerateName.GenerateName(count_write)
        list_SNIlS = GenerateSNILS.GenerateListSNILS(count_write)
        list_birthday = GenerateBirtday.GenerateBirthday(count_write)
        help_list = []
        for i in range(count_write):
            FIO = list_names[i][2] + " " + list_names[i][0] + " " + list_names[i][1]
            help_list.append(list_names[i][2])
            help_list.append(list_names[i][0])
            help_list.append(list_names[i][1])
            help_list.append(list_SNIlS[i])
            help_list.append(list_birthday[i])
            fake_db_writer.writerow(help_list)
            help_list.clear()
        already_write_in_fake_db += count_write
    fake_db.close()
    fake_db = open('original_db.csv', encoding='utf-8', mode='r')
    fake_db_writer = csv.reader(fake_db, delimiter=';')
    print(list(fake_db)[0].split(';'))


if __name__ == "__main__":
    genrateInput()
Anonymize('original_db.csv')
