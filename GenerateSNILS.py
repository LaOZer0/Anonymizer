import random


def CalculateSumSNILS(SNILS_num: str) -> int:
    sum_num_SNILS = 0
    position_num = 0
    for num in SNILS_num:
        position_num += 1
        if num != '-':
            sum_num_SNILS += int(num) * position_num
    return sum_num_SNILS


def MakeControlSum(sum_SNILS: int) -> str:
    if sum_SNILS == 100 or sum_SNILS == 101:
        return ' 00'
    if len(str(sum_SNILS % 101)) == 1:
        return ' 0' + str(sum_SNILS % 101)
    return ' ' + str(sum_SNILS % 101)


def GenerateListSNILS(count: int) -> list:
    string = '0123456789'
    set_SNILS = set()
    while len(set_SNILS) != count:
        SNILS = ''
        for i in range(9):
            if i == 2 or i == 5:
                SNILS += random.choice(string) + '-'
            else:
                SNILS += random.choice(string)
        SNILS += MakeControlSum(CalculateSumSNILS(SNILS))
        set_SNILS.add(SNILS)
    return list(set_SNILS)