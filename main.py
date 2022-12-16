import random

import time

import pandas as pd


def YQYSF():

    a = random.randint(0,1)

    b = random.randint(0,1)

    c = random.randint(0,1)

    global sum1

    sum1 = a + b + c
    
#     print(sum1)

    return a,b,c

#本卦

def BenG(li):

    yang = '________'

    yin = '___ ___'

    global xu1

    xu1=[]

    for _ in li:
        if _ == 0:
            print(yin + '*')
            xu1.append('YIN')
        elif _ == 1:
            print(yang)
            xu1.append('YANG')
        elif _ == 2:
            print(yin)
            xu1.append('YIN')
        elif _ == 3:
            print(yang + '*')
            xu1.append('YANG')
            
#     print("BenGxu1:",xu1)

#变卦

def BianG(li):

    yang = '________'

    yin = '___ ___'

    global xu2

    xu2=[]

    for _ in li:
        if _ == 0:
            print(yang)
            xu2.append('YANG')
        elif _ == 1:
            print(yang)
            xu2.append('YANG')
        elif _ == 2:
            print(yin)
            xu2.append('YIN')
        elif _ == 3:
            print(yin)
            xu2.append('YIN')
#     print("BianG",xu2)

#卦辞，文件是我自己收集的

def 八卦(卦):
    """将三个爻转化为一个八卦"""
    卦.reverse()
    r = 0
    for i,x in enumerate(卦):
        if x == "YANG":
            r += 2**i
    BaGua = ['地', '山', '水', '风', '雷', '火', '泽', '天']
#     print("1:",BaGua[r])
    return BaGua[r]

def 解(卦):
    """解卦，根据所占的六十四卦，在guaci.txt中寻找对应的卦辞并输出。
    卦辞来源百度"""
    下 = 八卦(卦[0:3])
#     print("下:",下)
    上 = 八卦(卦[3:])
#     print("上:",上)
    dic = {'地': '坤', '山': '艮', '水': '坎', '风': '巽',
           '雷': '震', '火': '离', '泽': '兑', '天': '乾'}
    if 上 == 下:
        卦名 = dic[下] + '为' + 下
        print("123:",卦名)
    else:
        卦名 = 上 + 下
#         print("1233:",卦名)
    filename = 'D:\guaci.txt'
    with open(filename,'r') as f:
        for i in range(500):
            s = f.readline()
            if 卦名 in s:
                return s



#主函数

def main():

    input('您要占卜的问惑：')

    print('请稍候，系统正在为您演算。')

    sum11=[]

    for i in range(1,7):

        time.sleep(1)

        print('第' + str(i) + '次的银钱演算结果是')

        print(YQYSF())

        sum11.append(sum1)       

    sum11.reverse()
    
    print(sum11)
    
    print('本卦是：')
    
    time.sleep(1)

    BenG(sum11)

    print('变卦是：')

    time.sleep(1)

    BianG(sum11)

    print('您本次的问卦结果是：')

    time.sleep(1)

    print('本卦：')

    卦=(xu1)
    卦.reverse()
    print(解(卦))

    print('变卦：')

    卦=(xu2)
    卦.reverse()
    print(解(卦))

    print('仅供参考')

if __name__ == '__main__':
    main()
