#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : Logger.py
# @Author: Liaop
# @Date  : 2019-05-08
# @Desc  : 通用日志类

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from src.utility.Global import Global


def getLogger(name, console=True):
    base_path = Global.base_path
    level = Global.config.log.level
    file = Global.config.log.file
    if level == 'debug':
        level = logging.DEBUG
    elif level == 'info':
        level = logging.INFO
    else:
        level = logging.DEBUG
    if not file:
        file = 'logs/info.log'
    path = os.path.dirname(file)
    if not os.path.isabs(path):
        path = os.path.join(os.path.abspath(base_path), path)
    if not os.path.exists(path):
        os.makedirs(path)
    file = os.path.join(os.path.abspath(base_path), file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = TimedRotatingFileHandler(file, 'H', 20, 0, encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if console:
        logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


