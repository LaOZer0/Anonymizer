import csv
from generators import generate_fake_db
from hasher import COUNT_WRITE, DbHasher



def Anonymize(path: str):
    next(hasher)
    next(hasher)
    print(hasher)
    print("penis")
    next(hasher)
    print(hasher)
    with open(path, encoding="utf-8", mode='r') as original_db:
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
    generate_fake_db("gen.csv")
