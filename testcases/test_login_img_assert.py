#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 11:02 PM
# @Author: Chaoran Lu

from time import sleep

import pytest

from page.LoginPage import LoginPage


class TestLoginAssert:
    @pytest.mark.login
    def test_login_assert(self, driver):
        """
        登陆后断言图片
        :param driver:
        :return:
        """
        LoginPage().login(driver, "william")
        sleep(3)
        assert LoginPage().login_assert(driver, "head_img.png") > 0.9

