n = int(input('ban muon nhap bao nhieu phan tu vao list 1 va 2, vui long nhap so  : '))
list = []
list2 = []
list3 = []
for i in range (1,n+1):
    a = input('nhap phan tu list1 thu 1 ')
    list.append(a)
for i in range (1,n+1):
    a = input('nhap phan tu list2 thu 2 ')
    list2.append(a)
for i in range(len(list)):
    for j in range(len(list2)):
        if list[i] == list2[j]:
            list3.append(list[i])
print(list3)



 
