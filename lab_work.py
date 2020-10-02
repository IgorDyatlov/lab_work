from pymorphy2 import MorphAnalyzer
from nltk.tokenize import word_tokenize

def add_to_dict(info, loop, counter, length):
    if counter == length:
        if type(loop) != list:
            loop[info] = list()
    else:
        loop[info] = dict()

def pymorphying(filename):
    dictionary = dict()
    morph = MorphAnalyzer()
    words_and_grams = list()
    with open(filename, 'r', encoding = 'utf-8') as file:
        text = file.read()
        tokenized = word_tokenize(text)
        for one in tokenized:
            parsed = morph.parse(one)
            parsed = parsed[0]
            original_word = one
            gram_info = str(parsed.tag).split(',')
            first_gram = str(gram_info[0]).split()[0]
            if first_gram == 'PNCT' or first_gram == 'UNKN':
                continue
            if len(gram_info) == 1:
                continue
            loop = dictionary
            counter = 0
            for gram in gram_info:
                counter += 1
                check = gram
                checking = check in loop
                if checking == False:
                    add_to_dict(check, loop, counter, len(gram_info))
                if type(loop) != list:
                    loop = loop[check]
            try:
                loop.append(original_word)
                loop.sort()
            except AttributeError:
                loop = list()
                loop.append(original_word)
                loop.sort()
    print(dictionary)
    
if __name__ == '__main__':
    filename = str(input('Введите название файла или путь к файлу (без кавычек):'))
    pymorphying(filename)
