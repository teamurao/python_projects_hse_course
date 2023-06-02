import re
from math import ceil

filename = 'The Coca-Cola Company — Википедия.html'


def opening(filename):
    with open(filename, encoding='utf-8') as f:
        file = f.read()
    return file


def regular(file):
    pattern = '<table class="wikitable">(.*?)</table>'
    result = re.search(pattern, file, re.S | re.M)
    result = result.group()
    return result


def regular_2(result):
    pattern = r'<th>(.*?)</th>'
    result_2 = re.findall(pattern, result, re.M)

    pattern = r'^<th>([0-9]*)$'
    result_21 = re.findall(pattern, result, re.M)

    first = '|'.join(result_2 + result_21)
    return first


def regular_3(result):
    pattern = r'<td>(.*?)</td>'
    second = re.findall(pattern, result, re.M)

    pattern = r'<td>([А-ЯЁа-яё ]+?)</td>'
    third = re.findall(pattern, result, re.M)

    parts = len(third)
    part_len = ceil(len(second) / parts)
    tabl = [second[part_len * k:part_len * (k + 1)] for k in range(parts)]

    return tabl


def main():
    file = opening(filename)
    result = regular(file)
    first = regular_2(result)
    tabl = regular_3(result)

    with open('table.txt', 'w', encoding='utf-8') as t:
        t.write(first)
        for row in tabl:
            t.write('\n')
            t.write('|\t'.join(row))
            t.write('\n')

    print(first)
    for row in tabl:
        print('|'.join(row))


if __name__ == '__main__':
    main()
