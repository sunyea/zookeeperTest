#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : zookeeperTest.py
# @Author: Liaop
# @Date  : 2019-06-25
# @Desc  : 主程序

from src.utility.Logger import getLogger
from src.utility.Config import getConfig
from src.utility.Global import Global
from src.zk.Master import Master
import sys, time


def main(conf_file):
    getConfig(conf_file)
    if not Global.config:
        return '无法获取配置信息，你指定的配置文件：{}不存在或是默认配置文件缺失'.format(conf_file)
    if 'log' not in Global.config.keys():
        return '无法获取日志记录的配置信息'
    logger = getLogger('Main')
    logger.debug('获取配置：{}'.format(Global.config))
    try:
        master = Master()
        is_master = master.is_master
    except Exception as e:
        return '启动master出错：{}'.format(e)
    while True:
        if is_master != master.is_master:
            print('角色发生了变化,master从{}变为{}'.format(is_master, master.is_master))
            is_master = master.is_master
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        conf_file = None
    else:
        conf_file = sys.argv[1]
    rt = main(conf_file)
    print(rt)
