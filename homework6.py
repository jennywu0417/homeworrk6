    
def sam (a,num):
    small = 100
    indexsmall = 0
    for i in range(1,2*a,2):
        if num[i] < small:
            small = num[i]
            indexsmall = num[i-1]
    print(indexsmall,'最低分:', small)

def big (a,num):
    biggest = 0
    indexbig = 0
    for i in range(1,2*a,2):
        if num[i] > biggest:
            biggest = num[i]
            indexbig  = num[i-1]
    print(indexbig,'最高分: ', biggest)

def avg1 (a,num):
    d = 0
    for i in range(1,2*a,2):
        d = d + num[i]
#print('sum: ',d)
    avg = d/a
    print('平均分:',avg)


a = int(input('請輸入班級人數:'))
name = []
num = []
for i in range(a):
    stu = input('請輸入姓名:')
    num.append(stu)
    e = int(input('請輸入分數:'))
    num.append(e)

#print(num)
avg1(a, num) 
big(a, num)      
sam(a, num)




