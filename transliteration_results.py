import csv
import requests
# from pyarabic import araby
import arabic_reshaper
from langdetect import detect


def handle_arabic_strings(line):
    #This function takes the line from the file and returns a properly formatted string
    id = line[line.find('('):]
    id = id.strip()
    line = line[:line.find('(')]
    words = line.split('<space>')
    actual_line = ""
    for word in words:
        # print(word)
        letters = word.split(' ')
        actual_word = ''.join(letters)
        # lang = detect(actual_word)
        # if lang == 'ar':
        actual_word = arabic_reshaper.reshape(actual_word)
        actual_line += actual_word + " "
    # print(id + ' ' + actual_line)
    return actual_line

def slice(string):
    list1=[]
    list1[:0]=string
    return list1

hyp_strings = []
ref_strings = []
transliterate_link_ar2en = 'https://transliterate.qcri.org/ar2en/'
# with open('wp3/exp-20220509/E2E-conformer/ArzEn/sys.a/ArzEn_dev/score_cer/hyp.trn', encoding='utf-8') as hyp_file:
#         with open('wp3/exp-20220509/E2E-conformer/ArzEn/sys.a/ArzEn_dev/score_cer/ref.trn', encoding='utf-8') as ref_file:
#             for line in hyp_file:
#                 hyp_line = handle_arabic_strings(line)
#                 ref_line = handle_arabic_strings(ref_file.readline())
#                 hyp_strings.append(hyp_line)
#                 ref_strings.append(ref_line)



transliterate_link_ar2en = 'https://transliterate.qcri.org/ar2en/'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
with open('/Users/oumniachellah/Documents/WP3/injy_a4_hyp_with_id.txt', encoding='utf-8') as hyp_file:
    for line in hyp_file:
        id = line[line.find('('):]
        id = id.strip()
        line = line[:line.find('(')]
        line = line.strip()
        if line != '':
        # words = line.split('<space>')
            actual_line = ""
            # print(line)
            # for word in words:
            #     letters = word.split(' ')
            #     actual_word = ''.join(letters)
            #     actual_line += actual_word + " "
            # print(actual_line)
            for word in line.split(' '):
                if len(word) != 0:
                    actual_line += word + " "
            # actual_line = line
            # print(actual_line)
            translit_hyp = requests.get(transliterate_link_ar2en + actual_line).json()['results']
            translit_words = translit_hyp.split(' ')
            # This part eliminates transliterations of words that were originally in english:
            original_words = actual_line.split(' ')
            for i in range(len(original_words)):
                word = original_words[i]
                if word != '' and word[0] in ascii_lowercase:
                    translit_words[i] = word
            # print(' '.join(translit_words))
            print(' '.join(translit_words) + ' ' + id)
        # This part inserts spaces between the characters (will use the output for character error rate):
        # separate_char_str = ""
        # for word in translit_words:
        #     letters = slice(word)
        #     separate_char_str += ' '.join(letters) + " "
        # print(separate_char_str + ' ' + id)
        # j += 1
        # if j == 50:
        #     break