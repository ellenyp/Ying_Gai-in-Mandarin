with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.read()
resultDICT = {"Sentence: ": ""}

#以more 為關鍵字合併前後句
    #import re
    #sentences = re.split(r'more', List)
    #print(sentences)


row = []
word = "more"
file = open("new_ying_gai.txt", "w", encoding = "utf-8")

for i, line in enumerate(List, start = 1):
    #print(line)
    if word in line:
        a = i
        
        row.append(i)
    else:
        ()
    if i in row:
        print(line)
        file.write(line)
            
    file = open("ying_gai_finish.txt", "w", encoding = "utf-8")
    for sentence in sentences:
        file.write(sentence)
        file.write("\n")
        #print(sentence) 
file.close()
f.close()

