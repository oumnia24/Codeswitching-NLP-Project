import sys

translit_lines=open(sys.argv[1]).readlines()
translit_chars = open(sys.argv[2],'w')

def slice(string):
    list1=[]
    list1[:0]=string
    return list1

for line in translit_lines:
    separated_string = ""
    words = line.split(' ')
    for word in words:
        if len(word) ==0 or word[0]!='(':
            letters = slice(word)
            separated_string += ' '.join(letters) + " "
    separated_string += words[len(words) - 1]
    translit_chars.write(separated_string +"\n")
