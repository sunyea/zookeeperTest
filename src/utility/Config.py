#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : Config.py
# @Author: Liaop
# @Date  : 2019-06-25
# @Desc  : 通用配置类

import configparser
import os
from src.utility.Global import Global


class ConfigDict(dict):
    def __getattr__(self, item):
        if item in self.keys():
            return self[item]
        else:
            return None

    def __setattr__(self, key, value):
        self[key] = value


def getConfig(file_name=None):
    try:
        parser = configparser.ConfigParser()
        if not file_name:
            file_name = os.path.join(Global.base_path, 'conf/default.cfg')
        parser.read(file_name)
        Global.config = ConfigDict()
        for section in parser.sections():
            Global.config[section] = ConfigDict()
            for key in parser[section]:
                Global.config[section][key] = parser.get(section, key)
    except Exception:
        Global.config = ConfigDict()
