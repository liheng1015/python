def matable(n=9):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('%sX%s=%s' %(j,i,j*i) , end=' ')
        print()
if __name__ == '__main__':
    m=input('请输入乘法表个数(默认9):')
    if m:
        m=int(m)
        matable(m)
    else:
        matable(9)

