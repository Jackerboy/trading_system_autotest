#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 4:44 PM
# @Author: Chaoran Lu

import random
import pytest

class TestRerun:
    @pytest.mark.flaky(reruns=50, reruns_delay=1)
    def test_rerun(self):
        num = random.randint(1, 50)
        print("num:", num)
        if num != 17:
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")
