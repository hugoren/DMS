#coding:utf-8
import  lbviews

def lb_sync(sync_conf):

    #迭代读一行
    def eachline(filename):
            with open(filename, 'rt') as handle:
                for lnno, line in enumerate(handle):
                    yield lnno, line


    server_list = str(lbviews.lb_list()).split(" ")
    print server_list
    writeback = []
    for line_no, line in eachline(sync_conf):
        if 'a' in line:
            line = 'b'+'\n'
        writeback.append(line)
    with open(sync_conf, 'wt') as handle:
        handle.writelines(writeback)

    print "内存持久化到nginx配置完成"

if __name__ == '__main__':

    lb_sync('/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf')