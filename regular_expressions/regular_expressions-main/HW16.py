import re

filename = input('Файл должен лежать там же, где и программа. Введите название файла (например, pour_out.txt): ')


def clear_text(filename):
    with open(filename, encoding='utf-8') as f:
        t = f.read()
        trash: str = ',./ ?(){}[]=+><!@#$%^&*:;"_`~|-\—1234567890«»'
        text = t.split()
        words = []
        for word in text:
            word = word.strip(trash).lower()
            if len(word) > 0:
                words.append(word)
    return words


def verb(words):
    words = clear_text(filename)
    result = []
    pattern = '^выл(ить|иться|ил|ила|ило|или|ью|ьешь|ьет|ьем|ете|ьют|ей|ьем|ьемте|ейте)$'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result


def participle_1(words):
    words = clear_text(filename)
    result = []
    pattern = '^выли(в|вши)'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result


def participle_2(words):
    words = clear_text(filename)
    result = []
    pattern = '^выливш(ий|его|ему|им|ем|ая|ей|ую|ею|ее|ие|их|ими|ись)$'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result


def participle_2_1(words):
    words = clear_text(filename)
    result = []
    pattern = '^вылит(ый|ого|ому|ым|ом|ая|ой|ую|ою|ое|ые|ых|ыми)$'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result


def participle_short(words):
    words = clear_text(filename)
    result = []
    pattern = '^выли(та|то|ты|т)$'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result


def verb_2(words):
    words = clear_text(filename)
    result = []
    pattern = '^выл(ился|илась|илось|ились|ьюсь|ьешься|ьется|ьемся|ьетесь|ются|ейся|ьемтесь|ейтесь)$'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result


def participle_2_2(words):
    words = clear_text(filename)
    result = []
    pattern = '^выливш(ийся|егося|емуся|имся|емся|аяся|ейся|уюся|еюся|ееся|иеся|ихся|имися)$'
    for word in words:
        if re.match(pattern, word):
            result.append(word)
    return result


def one_word(a, b, c, d, e, f, g):
    solut = a + b + c + d + e + f + g
    solution = []
    for word in solut:
        if word not in solution:
            solution.append(word)
    return solution


def main():
    words = clear_text(filename)
    a = verb(words)
    b = participle_1(words)
    c = participle_2(words)
    d = participle_2_1(words)
    e = participle_short(words)
    f = verb_2(words)
    g = participle_2_2(words)
    solution = one_word(a, b, c, d, e, f, g)
    print(solution)


if __name__ == '__main__':
    main()
