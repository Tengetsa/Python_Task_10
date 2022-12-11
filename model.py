# вычисления общего наименьшего знаменателя знаменателя
def lcm(num_1, num_2) -> int:
    i = max(num_1[1], num_2[1])
    while (i % num_1[1] != 0) or (i % num_2[1] != 0):
        i += 1
    return i


def parsing(my_str):
    if "/" in my_str:
        new_list = my_str.split("/")
    else:
        new_list = [my_str, 1]
    new_list = list(map(int, new_list))
    return new_list


# вычисление
def calculate(num_1: list, num_2: list, op: str) -> list:
    nok = lcm(num_1, num_2)
    cf_1 = nok // num_1[1]
    cf_2 = nok // num_2[1]
    if op == '+':
        return [num_1[0] * cf_1 + num_2[0] * cf_2, nok]
    elif op == '-':
        return [num_1[0] * cf_1 - num_2[0] * cf_2, nok]
    elif op == '*':
        return [num_1[0] * num_2[0], num_1[1] * num_2[1]]
    elif op == '/':
        return [num_1[0] * num_2[1], num_1[1] * num_2[0]]


def counting(oper, data):
    """
    Расчет рационального выражения
    :param oper:  оператор '+', '-', '/','*'
    :param data: веденные данные
    :return: результат расчета
    """
    new_list = data.split(oper)
    num_first = parsing(new_list[0])
    num_second = parsing(new_list[1])
    result = calculate(num_first, num_second, oper)
    return result
