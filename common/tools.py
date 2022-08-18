#! /usr/bin/python3
# coding=utf-8
# @Time: 8/16/2022 10:40 PM
# @Author: Chaoran Lu

import datetime
import os


def get_current_time():
    return datetime.datetime.now()


def get_project_path():
    """
    获取项目的绝对路径
    :return:
    """
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


if __name__ == '__main__':
    sep(["config", "environment.yaml"], add_sep_before=True)
