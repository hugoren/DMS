#coding:utf-8

import time
import sys
import os
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, FileTransferSpeed, FormatLabel, Percentage, \
  ProgressBar, ReverseBar, RotatingMarker, \
  SimpleProgress, Timer

def progress_test():
    bar_length=20
    for percent in xrange(0, 100):
        hashes = '#' * int(percent/100.0 * bar_length)
        spaces = ' ' * (bar_length - len(hashes))
        sys.stdout.write("\rPercent: [%s] %d%%"%(hashes + spaces, percent))
        sys.stdout.flush()
        time.sleep(1)

# progress_test()

def progress_bar():
    # 定义上传进度条样式
    widgets = ['Test: ', Percentage(), ' ',
              Bar(marker='#',left='[',right=']'),
              ' ', ETA(), ' ', FileTransferSpeed()]
    file_size = os.path.getsize('command_list')
    pbar = ProgressBar(widgets=widgets, maxval=file_size)
    # 开始进度条
    pbar.start()
    # 使用匿名方法接收上传返回值，并且显示进度条
    progress_bar = lambda transferred, toBeTransferred: pbar.update(transferred)
       # 使用匿名方法接收上传返回值，并且显示进度条
    progress_bar = lambda transferred, toBeTransferred: pbar.update(transferred)

progress_bar()