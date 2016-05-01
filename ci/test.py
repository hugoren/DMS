#coding:utf-8
import sys
import argparse

def read_argparse():
    parser = argparse.ArgumentParser(description="test")
    group = parser.add_argument_group()
    group.add_argument('-v','--verbose',help="v",action='store_true')
    group.add_argument('-a','--action',help='动作',action='store_true',dest='a')
    group.add_argument('app',help='发布的应用名称',action='store')
    group.add_argument('version',help='发布的版本' ,action='store')
    group.add_argument('-p','--publish',help='发布',action='store_true',dest='p')
    given_args = parser.parse_args()
    return given_args


if __name__ == '__main__':
    given_args = read_argparse()
    app = given_args.app
    action = given_args.a
    version = given_args.version
    publish = given_args.p
    print app +" "+ version