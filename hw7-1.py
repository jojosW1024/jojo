file = input()
populer_word = input()
former_list, latter_list = [], []
content = []
with open(file=file, mode='r', encoding='utf-8') as f:  # 寫入檔案
    for line in f:
        line = line.strip('\n')
        line = line.split('\t')
        for i in range(2):
            content.append(line[i].strip(' '))
print(content)



former = 0
latter = 0

for i in range(len(content)):
    if populer_word not in content[i]:
        continue
    else:
        sentence = content[i]
        while True:           
            index = sentence.find(populer_word)
            if index-1 >= 0:
                former = populer_word[0] if  str(sentence[index - 1])== '|' else str(sentence[index - 1])
                former_list.append(former)
            if index + len(populer_word) <= len(sentence)-1:
                latter = str(sentence[index + len(populer_word)]) 
                latter_list.append(latter)
            sentence = sentence.replace(sentence[index], '|', 1)
            while sentence.find(populer_word) == index:
                sentence = sentence.replace(sentence[index], '|', 1)
            if populer_word not in sentence:
                break
            else:
                continue


d_former = dict()
for element in former_list:
    if element not in d_former:
        d_former[element] = 1  
    else:
        d_former[element] += 1

d_latter = dict()
for element in latter_list:
    if element not in d_latter:
        d_latter[element] = 1  
    else:
        d_latter[element] += 1



sorted_former = sorted(d_former.items(), key=lambda s: (s[1], s[0]), reverse=True)
sorted_latter = sorted(d_latter.items(), key=lambda s: (s[1], s[0]), reverse=True)


print('熱門前一個字:')
for i in range(10):
    try:
        item_1 = sorted_former[i] 
        print(item_1[0] + '---' + str(populer_word))
    except:
        break

print('熱門下一個字:')
for i in range(10):
    try:
        item_2 = sorted_latter[i]
        print(str(populer_word) + '---' + item_2[0])
    except:
        break









