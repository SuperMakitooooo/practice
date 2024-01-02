import tkinter as tk
from pyperclip import paste
from pyperclip import copy 
import pathlib
import json
from .Base import base_viewer
from modules.console import console




class Clipboards(base_viewer):
	def __init__(self):
		super().__init__("clip.json") 	
	
		self.bind("<KeyPress>", self.console.run)

		self.console.body += [	{"keysym":"v", "state":console.Control_L,"function":self.paste},
					{"keysym":"c", "state":console.Control_L, "function":self.copy},
					{"keysym":"t", "state":console.Any, "function":print}]

	def down(self, self2=None):
		self.indices += 1
		self.change()

	
	def up(self):
		self.indices -= 1
		self.change()

	def paste(self):
		self.board[self.indices] = paste()
		print(paste())	
		self.Labels[self.indices].config(text=paste()[:15])


	def copy(self):
		clip =  self.board[self.indices]
		copy(clip)	

