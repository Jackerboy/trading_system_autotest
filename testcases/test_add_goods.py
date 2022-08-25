#! /usr/bin/python3
# coding=utf-8
# @Time: 8/24/2022 12:08 AM
# @Author: Chaoran Lu

from time import sleep

import pytest

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


goods_info_list=[
    {
        "goods_title": "Cybertruck",
        "goods_detail": "State of Art Electric Awesome Pick-up Truck!",
        "goods_num": 1,
        "goods_pic_list": ["商品图片一.jpg"],
        "goods_price": 69999,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
    {
        "goods_title": "Roadster",
        "goods_detail": "State of Art Electric Awesome Sports Car!",
        "goods_num": 1,
        "goods_pic_list": ["商品图片二.jpg"],
        "goods_price": 249999,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    }
]


class TestAddGoods:

    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_goods_001(self, driver, goods_info):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title=goods_info["goods_title"],
            goods_details=goods_info["goods_detail"],
            goods_num=goods_info["goods_num"],
            goods_pic_list=goods_info["goods_pic_list"],
            goods_price=goods_info["goods_price"],
            goods_status=goods_info["goods_status"],
            bottom_button_name=goods_info["bottom_button_name"]
        )
        sleep(3)
