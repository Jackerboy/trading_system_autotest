#! /usr/bin/python3
# coding=utf-8
# @Time: 8/17/2022 12:13 AM
# @Author: Chaoran Lu

from time import sleep

from config.driver_config import DriverConfig

driver = DriverConfig().driver_config()
driver.get("http://192.168.1.140/")
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
sleep(1)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(3)
driver.quit()
