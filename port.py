import json
import os
import pathlib

class port(pathlib.PurePath):
	def __init__(self, path):
		super().__init__(path)
		
		enc = "utf-8-sig" if self.suffix==".json" else "utf-8"

		try:
			f = open(path, "x", encoding=enc)
			f.close()
		except Exception as e:
			print(e)
			

	def load(self):
		if self.suffix == ".json":
			enc="utf-8-sig"
			loader = lambda f:json.load(f)
		else:
			enc="utf-8"
			loader = lambda f:f.read()

		with open(path, "r", encoding=enc) as f:
			return loader(f)			

	def save(self, content):
		if self.suffix == ".json":
			enc="utf-8-sig"
			writer = lambda f, content:json.dump(content, f)
		else:
			enc="utf-8"
			writer = lambda f,content: f.write(content)

		with open(path, "w", encoding=enc) as f:
			writer(f, content)			
