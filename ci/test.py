def hello(sn):
    def wrapper():
        t1 = "hello, %s" % sn.__name__
        print t1
        sn()
        print "goodby, %s" % sn.__name__
    return wrapper
 
@hello
def foo():
    print "i am foo rrrr"


def wrapper():
    t1 = "hello, %s" % 000
    print t1

foo()

wrapper()

