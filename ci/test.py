#coding:utf-8
#参数解释
import  sys

# def TestSys():
#     for arg in sys.argv[1:]:
#         print arg
# TestSys()

# import  argparse
# parser = argparse.ArgumentParser(description='test')
# args = parser.parse_args()


#形参，实参

def t1(a,b):
    print  a + b
t1(2,5)


def t2(c=3,d=9):
    print  c+d
t2()

def t3(*e):
    if len(e) == 0:
        print None
    else:
        print '%s_%s_%s'%(e[0],e[1],e[2])
t3(9,9,0)


def t4(**f):
    print f['a']

t4(a=99,b=88,c=77)


def t5():
    print "t5"
    def t6(y):
        print y
    t6("z")
t5()