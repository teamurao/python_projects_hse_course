# Настя Третьякова, 4 вариант

import random

print('Файл должен лежать в той же папке, что и программа.')

filename = 'words.csv'


def get_words(filename):
    with open(filename) as f:
        t = f.readlines()
        list_1 = []
        for i in t:
            list_2 = []
            sect = i.split(',')
            key = sect[0]
            clue = sect[1], sect[2], sect[3].strip('\n')
            list_2.append(key)
            list_2.append(clue)
            list_1.append(list_2)
        end_dict = dict(list_1)
    return end_dict


def clean_tip(end_dict):
    trash = ',./ ?(){}[]=+><!@#$%^&*:;"_`~|-\—1234567890«» '
    for word in tip:
        word = tip.strip(trash)
    return word


def puzzle(end_dict):
    k = list(end_dict.keys())
    answ = random.choice(k)
    tip = end_dict[answ][random.randint(0, 2)]
    trash = ',./ ?(){}[]=+><!@#$%^&*:;"_`~|-\—1234567890«»'
    for word in tip:
        ti = tip.strip(trash)
        t = ti.replace(' ', '')
    print('Поиграем? Я загадала слово и дам тебе одну подсказку:', tip, '.' * len(t))
    answer = input('Не жди у моря погоды! Действуй (напиши ответ): ')
    if answer == answ:
        print('Умничка!')
    else:
        print('Ошибочка вышла... Ну, ничего. Другое точно решится!')
    print('\t')


def main():
    while True:
        end_dict = get_words(filename)
        puzzle(end_dict)


if __name__ == '__main__':
    main()
