n = int(input('ban muon nhap bao nhieu phan tu vao list, vui long nhap so  : '))
list = []
for i in range (1,n+1):
    a = (input())
    list.append(a)
tong = 0
tich = 1
for j in range(0,len(list)):
    tong += list[j]
    tich *= list[j]
print ('tong = ',tong, ' tich = ', tich)
   

