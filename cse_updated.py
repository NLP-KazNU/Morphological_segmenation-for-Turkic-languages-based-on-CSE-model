import re
import os
import xlrd, xlwt
import pandas as pd

# прочитать файл с текстом (полностью)
with open("train.txt",  encoding="utf-8") as f:
    text_lines = f.readlines()
	
with open("stopwords", "r", encoding="utf-8") as f:
    tmp_stoplines = f.readlines() 

endings_wb = pd.read_excel("endings.xls", header=None, names=["Endings"])
endings_wb[['end1', 'end2']] = endings_wb['Endings'].str.split(' - ', expand=True)

endingsnew = list()
endingsnew_probel = list()

for i, row in endings_wb.iterrows():
    endingsnew.append(row['end1'])
    endingsnew_probel.append(row['end2'])

tmp_text_lines = []
new_words = []
stoplines = []
for ii in tmp_stoplines:
    if "\n" in ii:
        ii = ii.replace("\n", "")
    stoplines.append(ii)
j = 0

for line in text_lines:
    tmp_words = ""
    words = line.split()
    for word in words:
        j = 0
        found_in_stoplines = False
        for z in range(len(word), 1, -1):
            tubir=word[0:z]
            affix=word[z:]
            if tubir.lower() in stoplines:
                found_in_stoplines = True
                if affix in endingsnew:
                    index = endingsnew.index(affix)
                    affix = endingsnew_probel[index]
                    tmp_words += tubir + "@@ " + affix + " "
                    tmp_text_lines.append(tmp_words)
                    tmp_words = ""
                    #print("aaa: "+tubir+" + "+affix)
                    j += 1
                else:
                    tmp_words += tubir + affix + " "
                    tmp_text_lines.append(tmp_words)
                    tmp_words = ""
                    #print("bbb: "+tubir+" + "+affix)
                    j += 1
                break
            
        if not found_in_stoplines:
            if len(word) > 2:
                tubir = ""
                affix = ""
                for i in range(2,len(word)):
                    tubir=word[0:i]
                    affix=word[i:]
                    if affix in endingsnew:
                        index = endingsnew.index(affix)
                        affix = endingsnew_probel[index]
                        tmp_words += tubir + "@@ " + affix
                        tmp_text_lines.append(tmp_words)
                        tmp_words = ""
                        #print("eee: "+tubir+" + "+affix)
                        j += 1
                    else:
                        tmp_text_lines.append(word+" ")
                        #print("fff: "+word)
                        j += 1
                    break
                if j==0:
                    tmp_text_lines.append(word+" ")
                    #print("hhh: "+word)
            else:
                tmp_text_lines.append(word+" ")
                #print("ddd: "+word)
                
    tmp_text_lines.append('\n')
	
with open("result", "w", encoding="utf-8") as f:
    for line in tmp_text_lines:
        f.write('%s'%line)
