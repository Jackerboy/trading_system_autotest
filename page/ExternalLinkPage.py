#! /usr/bin/python3
# coding=utf-8
# @Time: 8/24/2022 2:32 PM
# @Author: Chaoran Lu

from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        """
        切换窗口为慕课网
        :param driver:
        :return:
        """
        self.switch_window_2_latest_handle(driver)
        return driver.title
