print('===================自制计算器====================')
a = float(input('请输入第一个数字:'))
b = input('请输入运算符(+,-,*,/):')
c = float(input('请输入第二个数字:'))
add = a + c
#减法
sub = a - c
#乘法
times = a * c
#除法
division = a / c

print('====================输出结果=====================')
if b == '+':
    print('您输入的加法运算结果为: %f'%add)

elif b == '-':
    print('您输入的减法运算结果为: %f'%sub)

elif b == '*':
    print('您输入的乘法运算结果为: %f'%times)

elif b == '/':
    print('您输入的除法运算结果为: %f'%division)
else :
    print('您输入的运算符有误！')
print('================================================')
