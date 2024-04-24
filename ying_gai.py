with open("ying_gai_raw.txt", "r", encoding = "utf-8") as f:
    List = f.read()
#print(List)

#合併奇偶句


#刪掉應該前最近的逗點以前的句子


#刪掉應該候最近的逗點以後的句子


#回傳最後結果到檔案


#data1 = List[List.index%2 == 0]
data1= List[[i%2==0 for i in range(len(List.index))]]

for i %2 ==0 in List.index [0:len(List)]:
    inputSTR = i
    data1 = List[[i%2 == 0]]
    data2 = List[List.index%2 == 1]
    