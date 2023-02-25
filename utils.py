COUNT_WRITE = 1000

def calculate_sumSNILS(SNILS_num: str) -> int:
    sum_num_SNILS = 0
    position_num = 0
    for num in SNILS_num:
        position_num += 1
        if num != '-':
            sum_num_SNILS += int(num) * position_num
    return sum_num_SNILS


def make_control_sum(sum_SNILS: int) -> str:
    if sum_SNILS == 100 or sum_SNILS == 101:
        return ' 00'
    if len(str(sum_SNILS % 101)) == 1:
        return ' 0' + str(sum_SNILS % 101)
    return ' ' + str(sum_SNILS % 101)

def get_pretty_row(names, birth, snils, sep=";") -> str:
    return sep.join([names[2], names[0], names[1], names[3], birth, snils]) + "\n"
