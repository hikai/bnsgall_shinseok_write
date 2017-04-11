# -*- coding: utf-8 -*-
"""
Script write today shinseok-shop in blade and soul gallery.

. . .
"""
from dcinside_mobile_write import DcWrite
from shinseokshop_parse import Parser

if __name__ == "__main__":
    obj_parse = Parser()
    parse_data = obj_parse.parse_data()

    str_result = ""
    for key in parse_data:
        str_result += "{}: {} 신석\n\n".format(key, parse_data[key])

    writer = DcWrite("bns", "오늘의 신석샵", "dkanehahfmsmsqlalfqjsgh", "★★오늘의 신석샵★★", str_result)
    writer.run()
