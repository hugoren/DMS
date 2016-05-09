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


def makeHtmlTag(tag,*arg,**kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"])\
        if "css_class" in kwds else ""

        def wrapped(*args,**kwds):
            return "<"+tag+css_class+">" + fn(*args,**kwds)+ "</"+tag+">"
        return wrapped
    return real_decorator


@makeHtmlTag(tag="b",css_class="bold_css")
@makeHtmlTag(tag="i",css_class="italic_css")
def hello():
    return "hello world"
print hello()