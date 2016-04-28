#coding:utf-8
import  lbviews

def lb_sync(sync_conf):

    #迭代读一行
    def eachline(filename):
            with open(filename, 'rt') as handle:
                for lnno, line in enumerate(handle):
                    yield lnno, line

    #获取upstream_servers列表
    servers = lbviews.lb_list()
    servers_list = servers.split("\n")
    #dict存储k=ip:port,v=server ip:port/down
    servers_dict ={}
    #为了精确匹配，取ip:port
    short_list = []
    for i in range(0,6):
        short_list.append(servers_list[i][7:22])
        servers_dict[servers_list[i][7:22]] = servers_list[i]



    #重新写入原文件
    writeback = []
    for line_no, line in eachline(sync_conf):
        for s in short_list:
            if s in line:
                line = servers_dict[s] + '\n'
        writeback.append(line)
        with open(sync_conf, 'wt') as handle:
            handle.writelines(writeback)

    print "内存持久化到nginx配置完成"

if __name__ == '__main__':

    lb_sync('/Users/hugo/PycharmProjects/Dsso/dtr/conf/nginx.conf')