import tkinter as tk
import random
import time
import json

class prepare:
	def __init__(self, master):
		self.master = master


	def config(self, configure = {"attr":"-topmost", "bg":"white", "geo":"600x200"}):
		self.master.attributes(configure["attr"], True)
		self.master.config(configure["bg"])
		self.master.geometry("configure["geo"])	


	def import_main_data(self, path):
		with open(path ,"r", encding="utf-8-sig") as f:
			return json.load(f)			
			

class Labels():
	def __init__(self, m, font="Times", fsize=30):
		self.labels = self.generate()
		self.all_pack()			


	def all_pack(self, position="anchor"):
		self.a.pack("anchor")
		self.b.pack("anchor")


	def generate(font_data, bg_color):
		return [tk.Label(text=None, font=font_data, bg=bg_color)]
			

class show(tk.Tk):
	dict = None

	s = random.sample 
	r = random.randint


	configure = {"attr":"-topmost", "bg":"white", "geo":"600x200", "wait":3000}

		
	path = ""

	def __init__(self):
		super().__init__()
		self.pre = prepere(self)

		self.pre.config(self.configure)
		self.dict = self.pre.import_main_data()

		self.labels = Labels(self)
		self.loop()

	
	def choose(self):
		l = len(self.dict)
		if l==0:
			self.dict = self.pre.import_main_data()
		k = self.dict.keys()
		keys = list(k)
		key = random.sample(keys, 1)[0]
		
		item = self.dict.pop(key)
		return (key, item)
	

	def set(self):
		key, item = self.choose()
		print(key, item)
		self.labels.a.config(text=key)
		time.sleep(self.wait["after_config_a"])
		self.labels.b.config(text=item)


	def loop(self): 
		self.set()
		super().after(self.wait["after_config_b"], self.loop)




