with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.readlines()
resultDICT = {"Sentence: ": ""}

#以more 為關鍵字合併前後句
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
            


f.close()
