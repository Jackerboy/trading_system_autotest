#! /usr/bin/python3
# coding=utf-8
# @Time: 8/17/2022 5:36 PM
# @Author: Chaoran Lu
import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self):
        return self.env["username"], self.env["password"]

    def get_url(self):
        return self.env["url"]


if __name__ == '__main__':
    print(GetConf().get_username_password())
