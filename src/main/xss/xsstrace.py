import os
import re
import subprocess
import time

class XssTrace(object):
    def __init__(self,url):
        super(XssTrace, self).__init__()
        self.url = url

    def execute_shell_command(self):
        command = ["python",
                   r"D:\PyCharmTest\PyCharmPackets\Models\WebScannerProject\reference\pythonProject\src\main\xss\XSSCon\xsscon.py",
                   "--single", self.url]
        # "./XSSCon/xsscon.py" 当前 但是要调用的时候 变成绝对路径
        current_time = time.localtime()
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", current_time)
        # output_file = "../../log/xss_log.txt"#.format(current_time)

        output_file = r"D:/PyCharmTest/PyCharmPackets/Models/WebScannerProject/reference/pythonProject/src/log/xss/xss_log_{}.txt".format(current_time)
        if not os.path.exists(output_file):
            open(output_file, 'w', encoding='utf-8').close()

        try:
            with open(output_file, "w", encoding='utf-8') as file:
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True,
                                                 encoding='utf-8')
                clean_data = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', output)
                split_text = clean_data.split("***************")

                if len(split_text) > 1:
                    extracted_content = split_text[1]
                else:
                    extracted_content = ""

                split_lines = extracted_content.split("\n")
                filtered_lines = [line for line in split_lines if line.strip()]  # 去掉空行
                result = "\n".join(filtered_lines)
                # print(result)
                file.write(result)
                # print("Success!")
                return result

        except subprocess.CalledProcessError as e:
            print(e.output)

# if __name__ == '__main__':
#     url = 'http://localhost:8080/pikachu/vul/xss/xsspost/post_login.php'
#     xss = XssTrace(url)
#     xss_log = xss.execute_shell_command()
#     print(xss_log)



