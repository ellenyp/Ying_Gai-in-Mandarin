# 提取含有關鍵字「應該」的句子
### 語料來源
進入[中央研究院平衡語料庫](https://asbc.iis.sinica.edu.tw/)網站，搜尋關鍵字「應該」。
### 如何提取句子
使用 **正規表示法(RE)** 
1. 將欲使用語料txt檔讀取進程式
2. 將原始資料以more拆分成多個字串
3. 再找出字串中所需句子的**pattern**後提取句子
4. 使用 **.replace** 將多餘換行及tab刪除，並使用 **.rstrip** 將句尾標點符號刪除
5. 定義**function**將單獨出現引號刪除
6. 將欲提取的句子以不重複為原則，寫出txt檔
### Content
```
+---intent
|       extract_ying_gai_final.py
|       test_ying_gai.py
|       ying_gai.py
|
\---txt
        new_ying_gai.txt
        ying_gai_finish.txt
        ying_gai_raw.txt
