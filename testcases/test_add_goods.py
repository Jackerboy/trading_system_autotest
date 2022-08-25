#! /usr/bin/python3
# coding=utf-8
# @Time: 8/24/2022 12:08 AM
# @Author: Chaoran Lu

from time import sleep

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:

    def test_add_goods_001(self, driver):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title="Cybertruck",
            goods_details="State of Art Electric Awesome Pick-up Truck!",
            goods_num=1,
            goods_pic_list=["商品图片一.jpg"],
            goods_price=49999,
            goods_status="上架",
            bottom_button_name="提交"
        )
        sleep(3)
