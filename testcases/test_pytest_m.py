#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 12:06 AM
# @Author: Chaoran Lu

from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:

    # @pytest.fixture(scope="class")
    # def scope_class(self):
    #     print("我是class级别， 我只执行一次")

    @pytest.fixture(scope="function")
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver

    @pytest.mark.extron
    def test_open_extron(self, driver):
        driver.get("https://www.extron.com")
        sleep(3)
        driver.quit()

    @pytest.mark.google
    def test_open_google(self, driver):
        driver.get("https://www.google.com")
        sleep(3)
        driver.quit()

    @pytest.mark.webull
    def test_open_webull(self, driver):
        driver.get("https://www.webull.com")
        sleep(3)
        driver.quit()