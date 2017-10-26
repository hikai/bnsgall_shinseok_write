#-*- coding: utf-8 -*-
"""
Shinseok recommend req.

@Hikai
"""
import requests

r = requests.get("http://a.bns.plaync.com/bnsapi/main/shop/displaygoods")
print(r.text)
