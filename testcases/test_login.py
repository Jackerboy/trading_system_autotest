#! /usr/bin/python3
# coding=utf-8
# @Time: 8/18/2022 10:44 PM
# @Author: Chaoran Lu

from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage

class TestLogin:

    def test_login(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(3)
        driver.quit()