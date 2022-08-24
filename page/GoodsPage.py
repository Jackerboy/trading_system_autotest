#! /usr/bin/python3
# coding=utf-8
# @Time: 8/23/2022 11:39 PM
# @Author: Chaoran Lu

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.GoodsBase import GoodsBase
from common.tools import get_img_path

class GoodsPage(GoodsBase, ObjectMap):

    def input_goods_title(self, driver, input_value):
        """
        输入商品标题
        :param driver:
        :param input_value:
        :return:
        """
        goods_title_xpath = self.goods_title()
        return self.element_fill_value(driver, By.XPATH, goods_title_xpath, input_value)