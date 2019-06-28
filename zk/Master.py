#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : Master.py
# @Author: Liaop
# @Date  : 2019-06-25
# @Desc  : 获取服务领袖

from kazoo.client import KazooClient
from utility.Logger import getLogger
from utility.Global import Global
import os


class Master(object):
    def __init__(self):
        self._logger = getLogger('Master')
        self._hosts = Global.config.zookeeper.hosts
        self._timeout = int(Global.config.zookeeper.timeout)
        self._root = Global.config.zookeeper.root
        self._master = '{}/master'.format(self._root)
        self.is_master = False

        self._zk = KazooClient(hosts=self._hosts, timeout=self._timeout)
        self._zk.start(timeout=self._timeout)
        self.__init_zk()
        self.register()
        self._zk.ChildrenWatch(self._master, func=self._watch_master)


    def __init_zk(self):
        nodes = (self._root, self._master)
        for node in nodes:
            if not self._zk.exists(node):
                try:
                    self._zk.create(node)
                except:
                    self._logger.error('创建节点：{}出错'.format(node))

    def _watch_master(self, children):
        children.sort()
        self._logger.debug('现有children: {}'.format(children))
        master = None
        if children:
            master = children[0]
        if master:
            if self._path == master:
                if self.is_master:
                    self._logger.info('我本来就是master')
                else:
                    self.is_master = True
                    self._logger.info('我成为了新的master')
            else:
                self._logger.info('{}是master, 我是slave'.format(master))

    def register(self):
        path = self._zk.create('{}/worker'.format(self._master), value=Global.myid, ephemeral=True, sequence=True)
        self._path = os.path.basename(path)
        self._logger.info('注册一个节点:{}'.format(path))

