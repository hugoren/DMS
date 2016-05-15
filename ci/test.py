# def hello(sn):
#     def wrapper():
#         t1 = "hello, %s" % sn.__name__
#         print t1
#         sn()
#         print "goodby, %s" % sn.__name__
#     return wrapper
#
# @hello
# def foo():
#     print "i am foo rrrr"
#
#
# def wrapper():
#     t1 = "hello, %s" % 000
#     print t1
#
# foo()
#
# wrapper()
#


# class myDecorator(object):
#     def __init__(self,fn):
#         print "inside myDecorator.__init__()"
#         self.fn = fn
#
#     def __call__(self):
#         self.fn()
#         print "inside myDecorator.__call__()"
#
# @myDecorator
# def aFunction():
#     print "inside aFunction()"
#
# aFunction
#
#
# def makeHtmlTag(tag,*arg,**kwds):
#     def real_decorator(fn):
#         css_class = " class='{0}'".format(kwds["css_class"])\
#         if "css_class" in kwds else ""
#
#         def wrapped(*args,**kwds):
#             return "<"+tag+css_class+">" + fn(*args,**kwds)+ "</"+tag+">"
#         return wrapped
#     return real_decorator
#
#
# @makeHtmlTag(tag="b",css_class="bold_css")
# @makeHtmlTag(tag="i",css_class="italic_css")
# def hello():
#     return "hello world"
# print hello()


# def t2():
#     name_len = map(len,["hao","xiang","ni"])
#     print name_len
#
#     name_list = ["hao","xiang","ni"]
#     for i in name_list:
#         print len(i)
#
# t2()
#
#
# def toUpper(item):
#     return item.upper()
# upper_name = map(toUpper,["hao","xiang","ni"])
# print upper_name
#
#
# def t3():
#     squares = map(lambda i:i * i,range(9))
#     print squares
# t3()
#
# def t4():
#     num = [0,-1,-3,-5,-8,7,3,9,10]
#     positive_num = filter(lambda x:x>0,num)
#     print positive_num
#     average = reduce(lambda x,y:x+y,positive_num)/len(positive_num)
#     print average
#
# t4()
#
#
#
# from random import  random
#
# def move_cars(car_position):
#     return map(lambda x:x+1 if random() > 0.3 else x,car_position)
#
# def output_car(car_position):
#     return '-' * car_position
#
# def run_step_of_race(state):
#     return {'time':state['time'] -1,'car_positions':move_cars(state['car_positions'])}
#
# def draw(state):
#     print ''
#     print '\n'.join(map(output_car,state['car_positions']))
#
# def race(state):
#     draw(state)
#     if state['time']:
#         race(run_step_of_race(state))
#
# race({'time':5,'car_positions':[1,1,1]})


import copy

# n1 = 123
# print  (id(n1))
#
#
# n2 = n1
# print (id(n2))
#
#
# n3 = copy.copy(n1)
# print (id(n3))
#
#
# n4 = copy.deepcopy(n1)
# print (id(n4))



# n1 = {"k1":"nick","k2":123,"k3":["jenny",666]}
# n2 = copy.deepcopy(n1)
# n3 = copy.copy(n1)
# print n2
# print n3


def name(n):
    print (n)

name(999)

def func(name,age=18):
    print("%s:%s")%(name,age)

func("hugo")


def fun1(*args,**kwargs):
    print args

fun1("ii","i9",["k1","hugo"],"00")


p = "nick"
def name():
    global p
    p = "jenny"
    print (p)

def name2():
    print p

name()
name2()