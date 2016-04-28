#coding:utf-8

import ConfigParser
import re
import os, sys
def t1():
    # cf = ConfigParser.ConfigParser()
    # cf.read("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf")
    # #return all section
    # secs = cf.sections()
    # print 'sections:', secs
    # print cf.items("A_running")
    # print cf.get("A_running","a_running")

    # f = open("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf","rb+")
    # f.truncate()
    # print "文件清空完成"
    # f.close()
    # f = open("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf","r+")
    # open('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream1.conf', 'w+').write(re.sub(r'server', 'upst 0000', f.read()))

    # data = """
    #    r24062 line1
    #    hello word !!!!
    #    r24729 line2 90943
    #    revision:24181 48983 1200012
    #    009
    #    008034
    #    09043949
    #    """
    # print data
    # r = re.compile("^r([0-9]{6,})", re.M)
    # nums = r.findall(data)
    # print nums


    # todo = {
    # 10: {'AAAA': '1.1.1.1'},
    # 20: {'BBBB': 'bbbbb'},
    # 30: {'#': ''},
    # }
    #
    # fp = open('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf',"r+")
    # data = ''
    # i = 0
    # for line in fp.readlines():
    #     i += 1
    #     if i in todo.keys():
    #         print 'line', i, line
    #         for key in todo[i]:
    #             line = line.replace('^'+key*, todo[i][key])
    #         print 'after replace:', line
    #     data += line
    # fp.close()
    # #保存在另一个文件
    # ret = open('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream1.conf','w+')
    # ret.write(data)
    # ret.close()

    # file = open("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf", "r+")
    # data = file.read()
    # re.sub("AAAA", "hugo", data)
    # file.close()
    # ret = open('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream1.conf','w+')
    # ret.write(data)
    # ret.close()


    # get=re.compile('bb');
    # w=lambda s : get.search("c") and 'cc\n' or s;
    # f=open('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream1.conf','rw');
    # ls=f.readlines();
    # f.close();
    # f = open('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream1.conf','r+')
    # all_lines = f.readlines()
    # for i in all_lines:
    #     print i

    # file = open("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream1.conf", "r+")
    # data = file.read()
    # # re.sub("AAAA", "new_content", data)
    # # re.s
    # save_file = open("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf", "w+")
    # for eachline in data:
    #     if 'a' in eachline:
    #         eachline = 'bc'
    #         print eachline
    #
    # save_file.write(data)
    # file.close()
    # save_file.close()

    def eachline(filename):
        with open(filename, 'rt') as handle:
            for lnno, line in enumerate(handle):
                yield lnno, line


    writeback = []
    for line_no, line in eachline('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf'):
        print line_no
        if 'a' in line:
            line = 'b'+'\n'
        writeback.append(line)
    with open('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf', 'wt') as handle:
        handle.writelines(writeback)

t1()