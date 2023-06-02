import re

print('Сейчас мы узнаем научную сферу вашего учёного.')
filename = input('Введите название html-файла: ')


def clean_text(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text


def regular(text):
    pattern = 'Научная сфера(.*?)</tr>'
    regularka = re.search(pattern, text, re.DOTALL)
    if regularka:
        reg = regularka.group()
    else:
        print('Самозванец! Никакой ты не учёный!')
    return reg


def scien_sph(reg):
    pattern = r'>[а-я].*?<'
    sph = re.findall(pattern, reg)
    return sph


def clean_sph(sph):
    trash = ',./ ?(){}[]=+><!@#$%^&*:;"_`~|-\—1234567890«»'
    words = []
    for word in sph:
        word = word.strip(trash).lower()
        if len(word) > 0:
            words.append(word)
            str(words)
            result = ', '.join(words)
    return result


def write(result):
    with open('scientific_sphere.txt', 'w', encoding='utf-8') as file:
        file.write(result)
    return file


def main():
    text = clean_text(filename)
    reg = regular(text)
    sph = scien_sph(reg)
    result = clean_sph(sph)
    file = write(result)
    print('Открой scientific_sphere.txt!')


if __name__ == '__main__':
    main()
