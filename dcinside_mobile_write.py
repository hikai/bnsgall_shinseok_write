# -*- coding: utf-8 -*-
"""
DCInside ariticle write script.

Mobile dcinside write.
"""
import json
import re
import requests
import time


class DcWrite():
    """DCinside article write class."""

    def __init__(self, id_gall, name, passwd, subject, contents):
        """
        Dcwrite initialize method.

        self.url = Dc gallery write page url.
        self.id_gall = gallery name.
        self.name = article author.
        self.passwd = article password.
        self.subject = article subject.
        self.memo = article contents.
        """
        self.url = "http://m.dcinside.com/write.php?id={}&mode=write"\
                   .format(id_gall)
        self.id_gall = id_gall
        self.name = name
        self.passwd = passwd
        self.subject = subject
        self.memo = contents

    def get_msg_data(self, option_data):
        """
        Method return msg data.

        req = request.
        """
        url = "http://m.dcinside.com/_option_write.php"
        self.session.headers["Referer"] = self.url
        self.session.headers["X-Requested-With"] = "XMLHttpRequest"
        while True:
            req = self.session.post(url, data=option_data)
            if req.text != '':
                return req.text

            time.sleep(1)

    def get_option_data(self):
        """
        Method return option_write data.

        data = post data for get block key.
        """
        data = dict()
        data["id"] = self.id_gall
        data["w_subject"] = self.subject
        data["w_memo"] = self.memo
        data["w_filter"] = 1
        data["mode"] = "write_verify"

        return data

    def get_code_value(self, html):
        """
        Method return code data in wrtie page.

        re_code = code value regex.
        """
        re_code = re.compile("name=\"code\" value=\"(.*?)\"")

        return re_code.findall(html)[0]

    def get_write_page(self):
        """Method return write page html."""
        return self.session.get(self.url).text

    def run(self):
        """
        Running method.

        code_token = mobile write page code value.
        msg = block key.
        """
        self.set_session()
        page = self.get_write_page()
        code_token = self.get_code_value(page)
        msg = json.loads(self.get_msg_data(self.get_option_data()))
        result = self.submit(code_token, msg["data"]).text

        if "refresh" in result:
            print("Success")
            print("http://gall.dcinside.com/{}".format(self.id_gall))
        else:
            print("Failed")
            print(result)

    def set_session(self):
        """
        Method set request sessio.

        self.session = request session value.
        """
        self.session = requests.session()
        self.session.headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1"

    def submit(self, code_token, msg):
        """
        Method last submit.

        url = write submit page url.
        data = post data.
        """
        url = "http://upload.dcinside.com/g_write.php"
        data = dict()
        data["name"] = (None, self.name)
        data["password"] = (None, self.passwd)
        data["subject"] = (None, self.subject)
        data["memo"] = (None, self.memo)
        data["user_id"] = (None, '')
        data["page"] = (None, '')
        data["mode"] = (None, "write")
        data["id"] = (None, self.id_gall)
        data["code"] = (None, code_token)
        data["no"] = (None, '')
        data["mobile_key"] = (None, "mobile_nomember")
        data["t_ch2"] = (None, '')
        data["FL_DATA"] = (None, '')
        data["OFL_DATA"] = (None, '')
        data["delcheck"] = (None, '')
        data["Block_key"] = (None, msg)
        data["filter"] = (None, '1')
        data["wikiTag"] = (None, '')

        return self.session.post(url, files=data)


if __name__ == "__main__":
    test = DcWrite("4", "이름", "비밀번호", "제목", "내용")
    test.run()
