#! /usr/bin/python3
# coding=utf-8
# @Time: 8/24/2022 10:13 PM
# @Author: Chaoran Lu

class IframeBaiduMapBase:

    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
