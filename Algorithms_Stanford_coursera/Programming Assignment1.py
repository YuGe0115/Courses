# 运用Recursive integer multiplication之上的Karatsuba算法，实现四次相乘→三次相乘（乘法的时间复杂度远大于加减法的时间复杂度）

def karatsuba(x,y): #此处只考虑x和y的长度一致的情况
    length = len(str(x))
    if length%2 == 1: #取余数来判断是否为奇数
        length += 1
    str_x,str_y = str(x),str(y)
    a = int(str_x[:(length//2)])
    b = int(str_x[(length//2):])
    c = int(str_y[:length//2])
    d = int(str_y[length//2:])

    return a*c*10**(length) + ((a+b)*(c+d) - a*c -b*d)*10**(length//2) + b*d

if __name__ == '__main__':
    x = int(input("第一个整数x："))
    y = int(input("第二个整数y："))
    print(karatsuba(x,y))
    