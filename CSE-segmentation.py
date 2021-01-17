# read train file
with open("PATH_TO_TRAIN-FILE\train",  encoding="utf-8") as f:
    text_lines = f.readlines()

# read all endings(affixes)
with open("endings", "r", encoding="utf-8") as f:
    text_endings = f.readlines()

with open("stop-words", "r", encoding="utf-8") as f:
    tmp_stoplines = f.readlines()

# delete '\n' from ending list 
tmp_text_endings = []
for item in text_endings:
    if "\n" in item:
        item = item.replace("\n", "")
    # добавляем пробелы после окончаний чтобы позже находились только окончания в конце слов
    tmp_text_endings.append(item + " ")
text_endings = tmp_text_endings

#для того чтобы показать вторую часть массива окончании из файла
endingsnew = list()
endingsnew_probel = list()
for item in text_endings:
    a, b = item.split(" - ")
    endingsnew.append(a)
    endingsnew_probel.append(b)

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
                    tmp_words += tubir + "@@ " + affix
                    tmp_text_lines.append(tmp_words)
                    tmp_words = ""
                   
                    j += 1
                else:
                    tmp_words += tubir + affix + " "
                    tmp_text_lines.append(tmp_words)
                    tmp_words = ""
                    
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
                        
                        j += 1
                    break
                if j==0:
                    tmp_text_lines.append(word+" ")
                    
            else:
                tmp_text_lines.append(word+" ")
                
                
    tmp_text_lines.append('\n')


# save the result to separate file
with open("train_segmented_CSE", "w", encoding="utf-8") as f:
    for line in tmp_text_lines:
        f.write('%s'%line)

print("1-process is over")        
