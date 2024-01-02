import json
import re


class arrange(list):
	def __init__(self):
		pass


	def flatten_viastr(lists):
		"""
		depend on eval and re.sub
		"""
		string = str(lists)[1:-1]
		string = re.sub("[", "", string)
		string = re.sub("]", "", string)
		return eval(string)

	
	def one_flatten(lists):
		for index, data in enumerate(lists):
			if type(data) == type(list()):
				lists = lists[:index] + data + lists[i+1:]
				break

	def flatten(lists):
		while lists == arrange.one_flatten(lists):
			lists = arrange.one_flatten(lists)
		return lists	
	
	





	

