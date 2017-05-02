list = []
for i in raw_input().split(' '):
    list.append(int(i))
temp1 = -999;
size =  len(list);
for i in range(0,size):
    for j in range(i+1,size):
        if list[i] < list[j]:
            temp2 = list[j]-list[i]
            if(temp2 > temp1):
                temp1 = temp2;
print temp1;
