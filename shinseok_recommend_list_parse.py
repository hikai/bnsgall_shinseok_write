# -*- coding: utf-8 -*-
"""
Shinseok recommend req.

@Hikai
"""
import json
import requests

class Parser_goods():
	"""Recommend goods parser."""

	def __init__(self):
		"""Initialize method."""
		self.url = "http://a.bns.plaync.com/bnsapi/main/shop/displaygoods"
		self.data = self.parse_data()
		print(json.loads(self.data.text))

	def parse_data(self):
		"""Parse goods data."""
		req = requests.get(self.url)

		return req

if __name__ == "__main__":
	goods = Parser_goods()
  
