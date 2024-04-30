with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.read()
    import re
    sentences = re.split(r'more', List)
    #print(sentences)
    
    # 正則表達式模式
    pattern = r'[「，。？∥]([^。，∥\n]*?\n應該\t.*?[：，。？∥])'
    
    # 提取符合模式的句子
    matching_sentences = []
    for sentence in sentences:
        matches = re.findall(pattern, sentence)
        matching_sentences.extend(matches)
    
    # 去除關鍵字「應該」前的換行及「應該」後的空白
    cleaned_sentences = [match.replace('\n', '').replace('\t', '').strip() for match in matching_sentences]

    # 輸出結果
    for sentence in cleaned_sentences:
        print(sentence) 
        
   
                                                    

    

    
        
        


#if __name__ == "__main__":
    


    