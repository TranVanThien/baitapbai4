n = int(input('ban muon nhap bao nhieu phan tu vao list, vui long nhap so  : '))
list = []
for i in range (1,n+1):
    a = input()
    list.append(a)
k = int(input('do dai list dau: '))
if k > len(list) :
    print(' ko hop le, ct ket thuc.')
else:
    list2 = []
    list2 = list[:k+1]
print (list2)
print (list[k+1:])