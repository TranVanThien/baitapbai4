n = int(input('nhap so luong muon them vao list = '))
list = []
for i in range (1,n+1):
    a = input()
    list.append(a)
print ('so lon nhat trong list = ', max(list), ' so nho nhat trong list = ', min(list))