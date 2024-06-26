with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.read()
    import re
    sentences = re.split(r'more', List)
    #print(sentences)
    
    # 正則表達式模式
    pattern = r'([^。，；：？∥\n]*?\n應該\t.*?[：，。？（∥])'
    
    # 提取符合模式的句子
    matching_sentences = []
    for sentence in sentences:
        matches = re.findall(pattern, sentence)
        matching_sentences.extend(matches)
    
    # 去除關鍵字「應該」前的換行、「應該」後的空白，句尾標點符號
    cleaned_sentences = [match.replace('\n', '').replace('\t', '').rstrip("，。？：（") for match in matching_sentences]

    #將上引號刪除，成對的引號則保留    
    for sentence in cleaned_sentences:
        def remove_quotes(sentence):
            if '「' in sentence and '」' in sentence:
                return sentence
            elif '「' in sentence:
                return sentence.replace('「', '')
            else:
                return sentence
        # 輸出結果
        #print(remove_quotes(sentence))    
    
    written_sentences = set()  # 用集合跟踪已經寫出的句子
    # 輸出結果至txt檔
    with open ("ying_gai_finish.txt", "w", encoding = "utf-8") as f:
        for sentence in cleaned_sentences:
                sentence = remove_quotes(sentence)
                if sentence not in written_sentences:
                    f.write(sentence + "\n")
                    written_sentences.add(sentence)
                    print (sentence)
                                                    

    

    
        
        


#if __name__ == "__main__":
    


    
