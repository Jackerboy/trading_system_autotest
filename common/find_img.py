#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 10:20 PM
# @Author: Chaoran Lu

import aircv as ac

from common.tools import get_project_path, sep


class FindImg:

    def img_imread(self, img_path):
        """
        读取图片
        :param img_path:
        :return:
        """
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        :param source_path: 原图路径
        :param search_path: 需要查找的图片的路径
        :return:
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)
        return result["confidence"]
