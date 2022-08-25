#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 2:55 PM
# @Author: Chaoran Lu

import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
