#! /usr/bin/python3
# coding=utf-8
# @Time: 8/16/2022 11:50 PM
# @Author: Chaoran Lu

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from common.tools import get_project_path, sep


class DriverConfig:
    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        options = webdriver.ChromeOptions()

        # 设置窗口大小为1920X1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动化测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL的错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 设置为无头模式(在不打开浏览器或Linux无UI的情况下)
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(ChromeDriverManager().install())
        # 删除所有cookies
        driver.delete_all_cookies()

        return driver
