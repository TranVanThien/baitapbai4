n = int(input('ban muon nhap bao nhieu phan tu vao list, vui long nhap so  : '))
list = []
for i in range (1,n+1):
    a = (input())
    list.append(a)
list2 = []
for i in range(len(list)):
    if list[i] not in list2:
        list2.append(list[i])
list2.sort()
print(list2)
