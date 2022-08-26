#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 9:16 PM
# @Author: Chaoran Lu

import pytest
from pytest_assume.plugin import assume


class TestAssert:
    def test_assert(self):
        with assume: assert "william" in "UI autotest"
        assert 1 + 1 == 2
        print("over")
