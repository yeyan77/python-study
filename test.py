#!/user/bin/python3

"""
import datetime
def getYesterday():
    today = datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

print(getYesterday())

#用户输入
x = input('输入x：')
y = input('输入y: ')
x,y = y,x
print('交换后的x: {}'.format(x))
print('交换后的y: {}'.format(y))


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False


print(is_number('foo'))
print(is_number('0.01'))
print(is_number('-22'))
print(is_number('10e3'))

print(is_number('٥'))
print(is_number('四'))
print(is_number('๒'))
print(is_number('©'))


"""

#判断是否是质子
"""

num = int (input('请输入一个数字：'))

if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print(num,'不是质数')
            print(i,'乘以',num//i,' is ',num)
            break

    else:
        print(num,'is 质数')


else:
    print(num,'不是质数')

"""


#输出指定范围内素数

"""
lower = int(input('min:'))
upper = int(input('max:'))

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break

        else:
            print(num)
"""


#九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i,j,i*j),end='')
    print()
"""

#斐波纳契数列
"""
netms = int(input('need :'))

n1 = 0
n2 = 1
count = 2

if(netms <= 0 ):
    print('请输入正整数')
elif netms == 1:
    print('斐波纳契数列: ')
    print(n1)
else:
    print('斐波纳契数列: ')
    print(n1,',',n2,end=' , ')
    while count < netms:
        nth = n1 + n2
        print(nth,end=' , ')
        n1,n2 = n2,nth
        count += 1

"""

#check if is 阿姆斯特朗数
"""
num = int(input('num: '))

sum = 0

n = len(str(num))

temp = num
while temp > 0:
     digit = temp % 10
     sum += digit ** n
     temp //= 10

if num == sum:
    print(num," is 阿姆斯特朗数")
else:
    print(num," is not 阿姆斯特朗数")
"""

#获取指定期间内的阿姆斯特朗数
lower = int(input('lower:'))
upper = int(input('upper:'))

for num in range(lower,upper+1):
    sum = 0
    n = len(str(num))

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if num == sum:
        print(num)