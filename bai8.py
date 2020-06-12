n = int(input('ban muon nhap bao nhieu phan tu vao list, vui long nhap so  : '))
list = []
for i in range (1,n+1):
    a = (input())
    list.append(a)
s = 0 
for i in range(0,len(list)):
   for j in range(1,len(list)):
        if i < j and list[i] > list[j]:
            s+=1
print('ok',s)