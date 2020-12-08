# 輸入資料並切割
num_and_weigh = input().split(',')
weigh = input().split(',')
value = input().split(',')
# 分別取出重量上限和物品數量
weigh_limit = int(num_and_weigh[1])
num = int(num_and_weigh[0])

cp_list = []  # assign 一個空list
for i in range(num):
    weigh[i] = int(weigh[i])
    value[i] = int(value[i])
    cp = value[i]/weigh[i]  # 計算cp值
    cp_list.append(cp)  # 將每次算出的cp值加入list

cp_sort = sorted(cp_list, reverse=True)  # 由大排到小

total_weigh = 0
take_it = []  # assign 一個空list
for i in range(num):
    cp_each = cp_sort[i]  # 依序由大到小提出各個cp值
    choose = cp_list.index(cp_each)  # 由大到小依序尋找原本cp值所在位置
    total_weigh += weigh[choose]  # 計算每次重量
    if total_weigh <= weigh_limit:
        take_it.append(choose+1)  # 若仍未超過上限，則代表此編號物品可以放入背包
    if total_weigh > weigh_limit:
        total_weigh -= weigh[choose]  # 若超過上限，須將先前多加的重量減掉

take_it.sort()  # 由小到大排列
for u in take_it:
    if u != take_it[-1]:
        print(u, end=',')  # 若不是最後一個數，皆要印出數字加逗號
    else:
    	print(u)  # 若是最後一個數則不需有逗號