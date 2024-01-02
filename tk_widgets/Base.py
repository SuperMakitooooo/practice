import tkinter as tk
from pyperclip import paste
from pyperclip import copy 
import pathlib
import json
from modules.data_manager import data_saver
from modules.console import console

class loop_list(list):
	def __init__(self, array):
		assert type(array) == type(list())
		self.body = array			

	def __getitem__(self, index):
		return self.body[index%len(self.body)]
		
	def __len__(self):
		return len(self.body)

	def __setitem__(self, key, value):
		self.body[key%len(self.body)] = value

	def __repr__(self):
		return str(self.body)

	def __iter__(self):
		return iter(self.body)



class base_viewer(tk.Tk):
	board = loop_list([i for i in range(10)])
	indices = 0
	path = ""

	def __init__(self, path):
		super().__init__()
		self.saver = data_saver(path)
		self.load()
	

		self.attributes("-topmost" , True)
		self.pos = 1 + 1j	


		self.Labels = loop_list([tk.Label(self, text=self.board[i]) for i in range(10)])
		[label.grid() for label in self.Labels]


		self.console = console()
		self.console.body = [		{"keysym":"Down", "state":console.Any, "function":self.down},
					{"keysym":"Up", "state":console.Any, "function":self.up},
					{"keysym":"q", "state":console.Control_L, "function":self.exit},
					{"keysym":"Tab", "state":console.Control_L, "function":self.move}]
	

		self.bind("<KeyPress>", self.console.run)


	def down(self, self2=None):
		print(self, self2)
		self.indices += 1
		self.change()

	
	def up(self):
		self.indices -= 1
		self.change()

	def change(self):
		change = self.Labels[self.indices]
		change.config(bg="black", fg="white")
		[label.config(bg="white", fg="black") for label in self.Labels if label != change]

	def exit(self):
		self._save()
		self.destroy()


	def move(self):
		self.pos *= 1j
		x = str(int(self.pos.real))
		y = str(int(self.pos.imag))
		
		if self.pos.real>=0:
			x = "+" + x
		
		if self.pos.imag>=0:
			y = "+"+ y


		self.geometry(x+y)


	def _load(self):
		self.board = loop_list(self.saver.load())

	def _save(self):	
		self.saver.save(self.board)

