import numpy as np
import json

def o():
	with open("study_tools/word.json","r",encoding="utf-8-sig")  as f:
		return json.load(f)


class compiler:
	def __init__(self, imported_dict):
		self.base = imported_dict
		self.keys= list(self.base.keys()	)


	def choosed_word(self):
		return self.base[self.keys.pop()]


	def all_search(self, word):
		result = []
		for key in self.base:
			if self.base[key] == word:
				result.append(key)

		return {word:result}


	def fuse(self,dict_list):
		"""
		from
		[dict, dict, dict, ,,, ]
		to
		{dict}
		"""
		result = dict()
		for i in dict_list:
			result.update(i)

		return result



	def filter_key(formula, dicts):
		""" use re expression"""
		result = []
		for key in dicts:
			if mono.filter(formula, key):	
				result.append(key)
		return result
		
		
	def filter_by_key(formula, dicts):
		result = dict()
		for key in compiler.filter_key(formula, dicts):
			result.update({key:dicts[key]})
		return result
		

	def filter_value(formula, dicts):
		result = []
		for key,value in dicts.items():
			if mono.filter(formula, value):
				result.append(key)
		return result


	def filter_by_value(formula, dicts):
		result = dict()
		for key in compiler.filter_value(formula, dicts):
			result.update({key:dicts[key]})
		return result
		





class mono:
	
	"""
	form  = "{} < 23"
	form.format({mono.distinguish:var})
	key < 2
	value == "aaa"
	value
	re.search,
	re.match("string", {})
	"""

	def filter(formula, item):
		return eval(formula.format("item"))

		




				