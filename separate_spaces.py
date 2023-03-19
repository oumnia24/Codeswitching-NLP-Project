import sys

to_sep =open(sys.argv[1]).readlines()


def slice(string):
    list1=[]
    list1[:0]=string
    return list1

for line in to_sep:
    words = line.split(' ')
    id = words[len(words) - 1]
    actual_line = ''
    for word in words:
        if len(word)== 0 or word[0] != '(':
            letters = slice(word)
            actual_line += ' '.join(letters) + ' , '
    actual_line += id
    print(actual_line)

