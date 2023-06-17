from spider.spider import Spider
from xss.xsstrace import XssTrace


class interface(object):
    def __init__(self):
        super(interface, self).__init__()

    def spider_interface(self, url):
        spi = Spider(url)
        url_list = spi.start(1)
        # print(url_list)
        return url_list

    def xss_interface(self, url):
        xss = XssTrace(url)
        xss_log = xss.execute_shell_command()
        # print(xss_log)
        return xss_log

# if __name__ == "__main__":
#     test = interface()
#     print(test.xss_interface("http://localhost:8080/pikachu/vul/xss/xsspost/post_login.php"))