#! /usr/bin/python3
# coding=utf-8
# @Time: 8/16/2022 10:40 PM
# @Author: Chaoran Lu

import datetime


def get_current_time():
    return datetime.datetime.now()


if __name__ == '__main__':
    print(get_current_time())
