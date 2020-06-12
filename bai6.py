n = int(input('ban muon nhap bao nhieu phan tu vao list, vui long nhap so  : '))
list = []
list2=[]
for i in range (1,n+1):
    a = str(input())
    list.append(a)
for i in range(0,len(list)):
    if len(list[i]) > 2:
        s = list[i]
        if s[0] == s[len(s)-1]:
            list2.append(list[i])
print (list2)

