import sys

sclite_lines=open(sys.argv[1]).readlines()
output_file=open(sys.argv[2],'w')
dict_scores={}

for line_index in range(0,len(sclite_lines)):
    line=sclite_lines[line_index].strip()
    if line.startswith("id:"):
        #id=line.split("(").replace(")","")
        scores_line=sclite_lines[line_index+1].strip()
        scores=scores_line.split()[-4:] #C #S #D #I
        # output_file.write("\t".join(scores)+"\n")
        word_error_rate = 0
        if int(scores[1]) + int(scores[2]) + int(scores[0]) != 0:
            word_error_rate = (int(scores[1]) + int(scores[2]) + int(scores[3]))/(int(scores[1]) + int(scores[2]) + int(scores[0]))
        else:
            word_error_rate = 1
        # print(scores)
        output_file.write(str(word_error_rate) +"\n")