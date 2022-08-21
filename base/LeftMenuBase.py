#! /usr/bin/python3
# coding=utf-8
# @Time: 8/20/2022 10:54 PM
# @Author: Chaoran Lu

class LeftMenuBase:

    def level_one_menu(self, menu_name):
        """
        一级菜单栏名称
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self, menu_name):
        """
        二级菜单名称
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"

