from russian_names import RussianNames
import random


def GenerateName(count: int) -> list:
    count_men = random.randint(0, count)
    count_women = count - count_men
    list_names = []
    list_men = RussianNames(gender=1, count=count_men, output_type='list').get_batch()
    list_women = RussianNames(gender=0, count=count_women, output_type='list').get_batch()
    for i in range(count_men):
        list_men[i].append('М')
        list_names.append(list_men[i])
    for i in range(count_women):
        list_women[i].append('Ж')
        list_names.append(list_women[i])
    return list_names