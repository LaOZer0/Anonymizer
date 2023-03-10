import random
import datetime
from russian_names import RussianNames
from .utils import *
from db import add_row
import cyrtranslit


GENERATION_PART = 100  # set 1000
TAILS = [
    "@yandex.ru", "@ya.ru", "@yandex.kz",
    "@mail.ru", "@yahoo.com", "@list.ru",
    "@gmail.com",
]
SEPARATORS = "._"


def random_yes():
    return bool(random.choice([0, 1]))


def c00l_1ine(string: str):
    result = ""
    for i in range(len(string)):
        if string[i] in "lo" and random_yes():
            result += "1" if string[i] == 'l' else "0"
        else:
            result += string[i]
    return result


def generate_email(firstname, lastname):
    count_chars = random.choice([1, len(firstname)])
    names = [firstname[:count_chars].lower(), lastname.lower()]
    names = [c00l_1ine(n) for n in names]
    names = [cyrtranslit.to_latin(n, "ru") for n in names]
    random.shuffle(names)
    sep = random.choice(SEPARATORS)
    return sep.join(names) + random.choice(TAILS)


def generate_birthday(count: int) -> list:
    dates = []
    for i in range(count):
        months = random.choice(
            ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
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
        list_men[i].append(1)
        list_names.append(list_men[i])
    for i in range(count_women):
        list_women[i].append(0)
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
        SNILS += make_control_sum(
            calculate_sumSNILS(SNILS)
        )
        set_SNILS.add(SNILS)
    return list(set_SNILS)


def generate_fake_db(count_rows: int = 1000000, step: int = 100):
    """
    generate_fake_db(filename: str, count_rows: int)
    generate fake db to filename csv
    @param filename: output file
    @param count_row: count rows in db
    """
    # for create file, if not exists
    # TODO :???????????????? ?????? ??????????????
    fake_db_size = 0
    for i in range(0, count_rows, step):
        count_write = min(step, count_rows - fake_db_size)
        list_names = generate_name(count_write)
        for names in list_names:
            add_row([
                names[0], names[1], names[2], names[3],
            ])
        fake_db_size += step
