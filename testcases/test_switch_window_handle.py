#! /usr/bin/python3
# coding=utf-8
# @Time: 8/24/2022 2:35 PM
# @Author: Chaoran Lu

from time import sleep

from config.driver_config import DriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage


class TestWindowHandle:

    def test_switch_window_handles(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "外链")
        sleep(1)
        title = ExternalLinkPage().goto_imooc(driver)
        print("title: ", title.encode("utf-8"))
        driver.quit()
