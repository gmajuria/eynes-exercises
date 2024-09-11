import random


def simple_list():
    dicts = []
    for i in range(1, 11):
        dicts.append({'id': i, 'age': random.randint(1, 100)})
    return dicts


def sort_list(dicts):
    return sorted(dicts, key=lambda x: x['age'])
