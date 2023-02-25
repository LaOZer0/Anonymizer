import random
import datetime
from russian_names import RussianNames
from utils import *

GENERATION_PART = 100 # set 1000

def generate_birthday(count: int) -> list:
    dates = []
    for i in range(count):
        months = random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
        year_today = datetime.date.today().year
        year = str(random.randint(year_today - 80, year_today - 15))
        if months == "02":
            day = random.randint(1, 28)
        elif months in ["04", "06", "09", "11"]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
        if day < 10:
            day = "0" + str(day)
        date = str(day) + "." + months + "." + year
        dates.append(date)
    return dates


def generate_name(count: int) -> list:
    count_men = random.randint(0, count)
    count_women = count - count_men
    list_names = []
    list_men = RussianNames(
        gender=1, count=count_men, output_type='list'
    ).get_batch()
    list_women = RussianNames(
        gender=0, count=count_women, output_type='list'
    ).get_batch()
    for i in range(count_men):
        list_men[i].append('М')
        list_names.append(list_men[i])
    for i in range(count_women):
        list_women[i].append('Ж')
        list_names.append(list_women[i])
    return list_names

def generate_listSNILS(count: int) -> list:
    string = '0123456789'
    set_SNILS = set()
    while len(set_SNILS) != count:
        SNILS = ''
        for i in range(9):
            if i == 2 or i == 5:
                SNILS += random.choice(string) + '-'
            else:
                SNILS += random.choice(string)
        SNILS += make_control_sum(calculate_sumSNILS(SNILS))
        set_SNILS.add(SNILS)
    return list(set_SNILS)

def generate_fake_db(filename: str, step: int = GENERATION_PART, count_rows: int = COUNT_WRITE):
    """
    generate_fake_db(filename: str, count_rows: int)
    generate fake db to filename csv
    @param filename: output file
    @param count_row: count rows in db
    """
    ## for create file, if not exists 
    # TODO :Передать ъто костыль
    with open(filename, "w", encoding="utf-8") as file:
        file.write("")
    fake_db_size = 0
    with open(filename, "a", encoding="utf-8") as file:
        for i in range(0, count_rows, step):
            count_write = min(step, count_rows - fake_db_size)
            list_names = generate_name(count_write)
            list_SNIlS = generate_listSNILS(count_write)
            list_birthday = generate_birthday(count_write)
            for i in range(count_write):
                file.write(get_pretty_row(
                     list_names[i], 
                     list_birthday[i],
                     list_SNIlS[i]
                ))
            fake_db_size += step

