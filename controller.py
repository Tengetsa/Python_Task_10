from model import *


def calculator(data: str):
    if '+' in data:
        oper = '+'
        return counting(oper, data)
    elif '-' in data:
        oper = '-'
        return counting(oper, data)
    elif '*' in data:
        oper = '*'
        return counting(oper, data)
    elif '/' in data:
        oper = '/'
        return counting(oper, data)
