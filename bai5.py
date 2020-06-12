n = int(input('ban muon nhap bao nhieu phan tu vao list, vui long nhap so  : '))
list = []
for i in range (1,n+1):
    a = (input())
    list.append(a)
max = 2 
b = []

for i in range(len(list)):
    if list.count(list[i]) >= max:
        max =  list.count(list[i])
        b.append(list[i])
    else:
        list2 = []
        list2.append(list[i])
        if list2 == list:
            print('cac phan tu khac nhau, chi xuat hien 1 lan ', list2)
        
     

