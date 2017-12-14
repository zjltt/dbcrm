#!/usr/bin/python
# -*- coding:utf-8 -*-

import hashlib

def encrypt(pwd):
    """
    :param pwd: 用户输入的明文密码
    :return: 通过md5加密之后生成的密码
    """
    obj = hashlib.md5()
    obj.update(pwd.encode('utf-8'))
    data = obj.hexdigest()
    return data