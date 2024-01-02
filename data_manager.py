import pathlib 
import json



def makefile(path, builtin_cls=[]):	
	if self.suffix == ".json":
		enc="utf-8-sig"
		f = open(path, "x", encoding=enc)
			json,dump([], f)
	else :
		enc="utf-8"
		f  =open(path, "x", encoding=enc)		
		f.close()	

	
class data_saver:
	def __init__(self, path):
		self.path = pathlib.PurePath(path)
		self.suffix = self._path.suffix
		self.full = str(self._path)
		print(self.full)
		makefile()		


	def load(self):
 		if self.suffix == ".json":
			self.enc="utf-8-sig"
			self.loader = lambda f:json.load(f)
		else:
			self.enc="utf-8"
			self.loader = lambda f:f.read()

		with open(self.full, "r", encoding=self.enc) as f:
			return self.loader(f)			


	def save(self, content):
		if self.suffix == ".json":
			enc="utf-8-sig"
			writer = lambda f, content:json.dump(content, f)
		else:
			enc="utf-8"
			writer = lambda f,content: f.write(content)

		with open(self.full, "w", encoding=enc) as f:
			writer(f, content)			
		


class builtin_manager:
	def __init__(self, path, main_cls, attr, sub_cls):
		self.cls = target[]
		

	def load(self):
		data = super().load()
		main_cls.__setattr_(attr, sub_class(data))
	

	def save(self):
		data = main_cls.__getattr__(attr)
		super().save(data)








class sync:
	def __init__(self, path, sub)


