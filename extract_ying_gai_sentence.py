with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.read()
    import re
    sentences = re.split(r'more', List)
    #print(sentences)
    
    for sentence in sentences:
                                                    pattern = r"[，。？∥、].*\n應該\t.*[，。？∥]"
                                                    matches = re.findall(pattern, sentence)                                                 
                                                    print(matches)
    extract_sentence = []
    for match in matches:
                                                    extract_sentence.append(match[1:])
                                                    print(extract_sentence)    
    

    
    
#List = ['共有 5092 筆資料\n\n', '次得獎後能夠引起經紀人的垂青。但他認為楊文信目前不\n應該\t放棄樂團的工作。國內愛樂人十二月十日將可一睹這位青']

#import re
#for sentence in List:
                                                #pattern = r"[，。？∥].*\n應該\t.*[，。？∥]"
                                                #matches = re.findall(pattern, sentence)
                                                ##print(matches)
#extract_sentence = []
#for match in matches:
                                                #extract_sentence.append(match[1:])
                                                #print(extract_sentence)
    
        
        


#if __name__ == "__main__":
    


    