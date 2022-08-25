#! /usr/bin/python3
# coding=utf-8
# @Time: 8/25/2022 1:06 PM
# @Author: Chaoran Lu

class TestAssert:
    def test_assert(self):
        # ==, !, <, >, <=, >=
        assert "chaoran" == "chaoran"
        assert "chaoran-a" != "chaoran-b"
        assert 0 < 1
        assert 2 > 1
        assert 3 <= 7 - 2
        assert 4 >= 1 + 2

        # 包含和不包含
        assert "chaoran" in "chaoran will take USC final exam"
        assert "chaoran" not in "UCLA computer science department"

        # true和false
        assert 1
        assert (9 < 10) is True
        assert not False