#! /usr/bin/python3
# coding=utf-8
# @Time: 8/24/2022 10:21 PM
# @Author: Chaoran Lu

from time import sleep

from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.IframeBaiduMapPage import IframeBaiduMapPage


class TestIframeBaiduMap:
    def test_iframe_baidu_map(self, driver):
        LoginPage().login(driver, "william")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(10)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        sleep(3)
