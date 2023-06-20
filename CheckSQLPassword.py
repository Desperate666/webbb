import sys


class CheckSQLPassword:
    def __init__(self):
        pass

    def do_check(self):
        print("")
        print("命令格式：check:-dbUrl -dbUser -passPath")
        print("dbUrl:远程数据库地址！\ndbUser:需要破解的账号\npassPath:字典文件路径\n")

        try:
            cmd = input().strip()  # 获取用户输入的命令
            if cmd.lower() != "exit":
                params = self.parse_cmd(cmd)  # 解析命令参数
                check = CheckSQLPasswordUtil(params[0], params[1], params[2])  # 创建实例
                check.do_check()  # 执行密码检查
            else:
                return
        except IOError:
            print("读取命令错误")

    @staticmethod
    def parse_cmd(cmd):
        params = [None] * 3
        token = cmd[cmd.index(":") + 1:].split("-")  # 提取参数部分并按照"-"分割
        for i in range(len(params)):
            params[i] = token[i].strip()  # 去除参数值的多余空格
        return params


class CheckSQLPasswordUtil:
    def __init__(self, db_url, db_user, pass_path):
        self.db_url = db_url
        self.db_user = db_user
        self.pass_path = pass_path

    def do_check(self):
        # TODO: 添加逻辑以检查 SQL 密码
        pass


if __name__ == "__main__":
    check_sql_password = CheckSQLPassword()
    check_sql_password.do_check()
