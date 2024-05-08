with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.read()
    import re
    sentences = re.split(r'more', List)
    #print(sentences)
    
    # 正則表達式模式
    pattern = r'([^。；，？∥\n]*?\n應該\t.*?[：，。？∥])'
    
    # 提取符合模式的句子
    matching_sentences = []
    for sentence in sentences:
        matches = re.findall(pattern, sentence)
        matching_sentences.extend(matches)
    
    # 去除關鍵字「應該」前的換行、「應該」後的空白，句尾標點符號
    cleaned_sentences = [match.replace('\n', '').replace('\t', '').rstrip("，。？：") for match in matching_sentences]

    # 輸出結果至txt檔
    #file = open("ying_gai_finish.txt", "w", encoding = "utf-8")
    for sentence in cleaned_sentences:
        ##file.write()
        #file.write(sentence)
        #file.write("\n")
        print(sentence) 
#file.close()
f.close()
   
                                                    

    

    
        
        


#if __name__ == "__main__":
    


    