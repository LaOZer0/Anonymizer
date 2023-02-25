import random
import datetime


def GenerateBirthday(count: int) -> list:
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