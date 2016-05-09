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


def t2():
    name_len = map(len,["hao","xiang","ni"])
    print name_len

    name_list = ["hao","xiang","ni"]
    for i in name_list:
        print len(i)

t2()


def toUpper(item):
    return item.upper()
upper_name = map(toUpper,["hao","xiang","ni"])
print upper_name


def t3():
    squares = map(lambda i:i * i,range(9))
    print squares
t3()

def t4():
    num = [0,-1,-3,-5,-8,7,3,9,10]
    positive_num = filter(lambda x:x>0,num)
    print positive_num
    average = reduce(lambda x,y:x+y,positive_num)/len(positive_num)
    print average

t4()