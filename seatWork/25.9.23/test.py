import math


print(1+2)
print(10+30.5)
print(10-30.5)
print(10*30.5)
x=14;y=4
print(x/y)
print(x//y)#//是整除
print(2**4)#**是次方
print(2**(1/2))#2开根号
print(10**1000)
print(5%2)#%取余数
print(23%5)

x=14;y=4;z=2
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(5>=4)
print(x>y & y>z)
print(z<y<x)
print(x>y &y<z)
print(x>y | y<z)

print(not x>y)
print(True)
print(False)
x=input("请输入一个数:")
print(x)
print(type(x))
print(x+10)
y=float(x)
print(type(y))
print(y+10)
print(x,y)
print('x=',x,'y=',y)
print('x={0},y={1}'.format(x,y))#?????????????
print(abs(-10))#绝对值
print(round(3.1415))#四舍五入取整
print(round(3.1415,2))#四舍五入，保留2位小数
print(2**5)
print(pow(2,5))

math.trunc(8.6) #截断小数，只保留整数
math.sqrt(2)#开根号
math.sqrt(16)

print(math.pi)
math.sin(30/360*2*math.pi)
math.sin(math.radians(30))

math.log10(10)
math.log10(100)#log10以10为底的对数

print(math.e)
math.log(2)
math.log(math.e)

math.log2(2)#以2为底数
math.log2(16)
