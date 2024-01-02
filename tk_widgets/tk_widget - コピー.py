import tkinter as tk
from pyperclip import paste
from pyperclip import copy 
import pathlib
import json
from data_manager import data_saver


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
	path = "data.json"

	def __init__(self):
		super().__init__()
		self.saver = data_saver(self.path)
		self.board = self.saver.load()

		self.attributes("-topmost" , True)

		self.Labels = loop_list([tk.Label(self, text=self.board[i]) for i in range(10)])
		[label.grid() for label in self.Labels]


		self.console = console()
		self.console.body = [	{"keysym":"Down", "state":console.Any, "function":self.down},
			{"keysym":"Up", "state":console.Any, "function":self.up},
			{"keysym":"q", "state":console.Control_L, "function":self.exit}]
	

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
		self.saver.save(self.board)
		self.destroy()


from modules.console import console




class Clipboards(tk.Tk):
	clips = loop_list([i for i in range(10)])
	indices = 0


	def __init__(self):
		super().__init__()

		self.attributes("-topmost" , True)
		self.Labels = loop_list([	
					tk.Label(self, text=self.clips[self.indices])
					for i in range(10)
				])

		[label.grid() for label in self.Labels]	
		self.console = console()
		self.bind("<KeyPress>", self.console.run)


		self.console.body = [	{"keysym":"Down", "state":console.Any, "function":self.down},
				{"keysym":"Up", "state":console.Any, "function":self.up},
				{"keysym":"v", "state":console.Control_L,"function":self.paste},
				{"keysym":"c", "state":console.Control_L, "function":self.copy},
				{"keysym":"t", "state":console.Any, "function":print}]

	def down(self, self2=None):
		print(self, self2)
		self.indices += 1
		self.change()
	
	def up(self):
		self.indices -= 1
		self.change()


	def paste(self):
		self.clips[self.indices] = paste()
		print(paste())	
		self.Labels[self.indices].config(text=paste()[:15])

	def copy(self):
		clip =  self.clips[self.indices]
		copy(clip)	


	def change(self):
		change = self.Labels[self.indices]
		change.config(bg="black", fg="white")
		[label.config(bg="white", fg="black") for label in self.Labels if label != change]
		

class task(base_viewer):
	board = loop_list([i for i in range(10)])
	indices = 0
	path = "data.json"

	

	def __init__(self):
		super().__init__()
		self.wm_attributes("-transparentcolor", "SystemButtonFace")
		self.overrideredirect(1)	
		self.geometry('-1-1')	

		self.entry = tk.Entry(self)
		self.entry.grid()

		self.timer = Timer(self)
		self.timer.grid()


		self.bind("<KeyPress>", self.console.run)

		

		self.console.body += [{"keysym":"i", "state":console.Control_L,"function":self.insert},
				{"keysym":"d", "state":console.Control_L, "function":self.delete},
				{"keysym":"s", "state":console.Control_L, "function":self.save}]


		self.console.body += [{"keysym":"Return", "state":console.Any, "function":self.timer.start},
				{"keysym":"space", "state":console.Any, "function":self.timer.stop},
				{"keysym":"BackSpace", "state":console.Any, "function":self.timer.reset},
				{"keysym":"Tab", "state":console.Any, "function":self.timer.set_task}]


	def insert(self):
		inp = self.entry.get()
		self.board[self.indices] = inp
		self.Labels[self.indices].config(text=inp)
		self.entry.delete(0, tk.END)			
		self.saver.load()


	def delete(self):
		self.board[self.indices] = 0
		self.Labels[self.indices].config(text=0)	
		self.saver.load()
	

	def save(self):
		self.saver.save(self.board)


		




import time

from modules.console import console
now = lambda : int(time.time())

class Timer(tk.Frame):
	
	def __init__(self, master, task=""):		
		self.master = master
		self.range = 60 * 3 
		
		super().__init__(master)
		self.display = tk.Label(self)
		self.task_displayer = tk.Label(self, text= task)

		self.display.grid()
		self.task_displayer.grid()

		self.set_default()		

		self.main()


	def set_default(self):
		self.progress = 0
		self.timer_running=0
		self.display.config(text="3:00")

	def main(self):
		"""
		>>> now() == int(time.time())
		True
		"""		
		if self.progress >= self.range:
			print("end")
			return

		if not self.timer_running:
			self.master.after(10, self.main)
			return 
		self.progress += (now() - self.time_stamp)
		self.time_stamp = now()

		string = self.converter(self.range -self.progress)
		self.load(string)
		self.master.after(10, self.main)
		

	def converter(self, progress):
		"""
		>>> Timer.converter("self", 60*20)
		'20:0'
		"""
	
		seconds = progress  % 60 
		minutes = progress // 60
		string = "{}:{}".format(minutes, seconds)
		return string


	def load(self, string):
		self.display.config(text=string)
		
	def set_task(self):
		self.task_displayer.config(text=self.master.board[self.master.indices])

	def start(self):
		self.timer_running=True
		self.time_stamp = now()

	def stop(self):
		self.timer_running=False
		
	def reset(self):
		self.set_default()
	
	def end(self):
		print("end")
		

		

def _test():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	_test()
