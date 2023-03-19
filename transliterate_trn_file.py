import requests
import sys

to_transliterate=open(sys.argv[1]).readlines()
lang = sys.argv[2]

if lang == 'ar':
    transliterate_link = 'https://transliterate.qcri.org/en2ar/'
elif lang == "eng":
    transliterate_link = 'https://transliterate.qcri.org/ar2en/'

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(to_transliterate)):
    line = to_transliterate[i]
    id = line[line.find('('):]
    id = id.strip()
    line = line[:line.find('(')]

    words = line.split('<space>')
    actual_line = ""
    for word in line.split(' '):
        if len(word) != 0:
            actual_line += word + " "
    if actual_line != "":
        translit_hyp = requests.get(transliterate_link + actual_line).json()['results']
        translit_words = translit_hyp.split(' ')
        # This part eliminates transliterations of words that were in original language:
        original_words = actual_line.split(' ')
        for i in range(len(original_words)):
            word = original_words[i]
            if lang == 'ar':
                if word != '' and word[0] not in ascii_lowercase:
                    translit_words[i] = word
            else:
                if word != '' and word[0] in ascii_lowercase:
                    translit_words[i] = word
        print(' '.join(translit_words) + ' ' + id)
    else:
        print(' ' + id)