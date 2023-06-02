#"Грамматичность" я понимаю как Хомский, т.е.
#Colorless green ideas sleep furiously. - грамматичное предложение

import random

def word_1():
    with open('1.txt', encoding='utf-8') as f:
        text = f.read()
        words1 = text.split()
        word1 = random.choice(words1)
        return word1
    
def word_2():
    with open('2.txt', encoding='utf-8') as f:
        text = f.read()
        words2 = text.split()
        word2= random.choice(words2)
        return word2

def word_3():
    with open('3.txt', encoding='utf-8') as f:
        text = f.read()
        words3 = text.split()
        word3 = random.choice(words3)
        return word3

def word_4():
    with open('4.txt', encoding='utf-8') as f:
        text = f.read()
        words4 = text.split()
        word4 = random.choice(words4)
        return word4

def word_5():
    with open('5.txt', encoding='utf-8') as f:
        text = f.read()
        words5 = text.split()
        word5 = random.choice(words5)
        return word5

def word_6():
    with open('6.txt', encoding='utf-8') as f:
        text = f.read()
        words6 = text.split()
        word6 = random.choice(words6)
        return word6

def word_7():
    with open('7.txt', encoding='utf-8') as f:
        text = f.read()
        words7 = text.split()
        word7 = random.choice(words7)
        return word7

def punct():
    marks = ['.', '!', '...']
    return random.choice(marks)

def string_1():
    string_1 = word_1().capitalize() + ' ' + word_2() + ' ' + word_3() + ' ' + word_6() + punct()
    print(string_1)

def string_2():
    string_2 = word_4().capitalize() + ' ' + word_1() + ' ' + word_5() + ' ' + word_3() + ' ' + word_2() + punct()
    print(string_2)

def string_3():
    string_3 = word_1().capitalize() + ' ' + word_5() + ' ' + word_3() + ' ' + word_7() + punct()
    print(string_3)

def main():
    string_1()
    string_2()
    string_3()

if __name__ == '__main__':
    main()
