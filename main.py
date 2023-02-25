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


def Anonymize(path: str):
    with open(path, encoding="utf-8", mode='r') as original_db:
        original_db_reader = csv.reader(original_db, delimiter=';')
        count = 0
        for _ in original_db_reader:
            count += 1
        len_fake_db = min(100000, count * 3)
        hashes = []
        flag = 0
        for row in original_db_reader:
            if flag == 0:
                flag += 1
            else:
                s_name = row[0].split()[0]
                f_name = row[0].split()[1]
                m_name = row[0].split()[2]
                hashes.append(HashToInt(hashFunction(s_name, f_name, m_name)) % 1000000014000000119 % len_fake_db)
        fake_db = open('fake_db.csv', encoding='utf-8', mode='r+')
        fake_db_writer = csv.writer(fake_db, delimiter=';', lineterminator="\r")
        already_write_in_fake_db = 0
        while len_fake_db - already_write_in_fake_db != 0:
            count_write = min(1000, len_fake_db - already_write_in_fake_db)
            list_names = GenerateName.GenerateName(count_write)
            list_SNIlS = GenerateSNILS.GenerateListSNILS(count_write)
            list_birthday = GenerateBirtday.GenerateBirthday(count_write)
            help_list = []
            for i in range(count_write):
                FIO = list_names[i][2] + list_names[i][0] + list_names[i][1]
                help_list.append(FIO)
                help_list.append(list_names[i][3])
                help_list.append(list_SNIlS[i])
                help_list.append(list_birthday[i])
                fake_db_writer.writerow(help_list)
                help_list.clear()
            already_write_in_fake_db += count_write

        first_line = list(original_db)[0].split(';')

        new_original_db = open(path, encoding='utf-8', mode='w')
        new_original_db_writer = csv.writer(new_original_db, delimiter=';', lineterminator="\r")
        fake_db_list = list(fake_db)
        new_original_db_writer.writerow(first_line)
        for i in range(len(hashes)):
            new_original_db_writer.writerow(fake_db_list[hashes[i] - 1].split(';'))
        fake_db.close()
        new_original_db.close()
    return 0


Anonymize('original_db.csv')
