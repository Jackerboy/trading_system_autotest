#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 12:06 AM
# @Author: Chaoran Lu

from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:

    @pytest.mark.extron
    def test_open_extron(self):
        print("test_open_extron")
        driver = DriverConfig().driver_config()
        driver.get("https://www.extron.com")
        sleep(3)
        driver.quit()

    @pytest.mark.google
    def test_open_google(self):
        driver = DriverConfig().driver_config()
        driver.get("https://www.google.com")
        sleep(3)
        driver.quit()