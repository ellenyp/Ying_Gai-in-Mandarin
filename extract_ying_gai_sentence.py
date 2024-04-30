with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.read()
    import re
    sentences = re.split(r'more', List)
    #print(sentences)
    
    # 正則表達式模式
    pattern = r'[「，。？∥]([^。，∥\n]*?\n應該\t.*?[，。？∥])'
    
    # 提取符合模式的句子
    matching_sentences = []
    for sentence in sentences:
        matches = re.findall(pattern, sentence)
        matching_sentences.extend(matches)
    
    # 輸出結果
    for match in matching_sentences:
        print(match)
        
    #for sentence in sentences:
                                                    #pattern = r"[，。？∥、].*\n應該\t.*[，。？∥]"
                                                    #matches = re.findall(pattern, sentence)                                                 
                                                    ##print(matches)
                                                    #extract_sentence = []
                                                    #for match in matches:
                                                                                                    #extract_sentence.append(match[1:])
                                                                                                    #print(extract_sentence)    
                                                    

    

    
        
        


#if __name__ == "__main__":
    


    