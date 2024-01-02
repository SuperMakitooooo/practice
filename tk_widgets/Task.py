import tkinter as tk
from modules.data_manager import data_saver
from .Base import base_viewer
from.Base import loop_list
import time
from modules.console import console



now = lambda : int(time.time())

	
class task(base_viewer):
	path = "data.json"

 	

	def __init__(self):
		super().__init__(self.path)
		#self.wm_attributes("-transparentcolor", "SystemButtonFace")
		#self.overrideredirect(1)	
		self.geometry('-1-1')	

		self.entry = tk.Entry(self)
		self.entry.grid()

		self.timer = Timer(self)
		self.timer.grid()


		self.bind("<KeyPress>", self.console.run)

		

		self.console.body += [{"keysym":"i", "state":console.Control_L,"function":self.insert},
				{"keysym":"d", "state":console.Control_L, "function":self.delete},
				{"keysym":"s", "state":console.Control_L, "function":self.save}]


		self.console.body += [{"keysym":"Return", "state":console.Control_L, "function":self.timer.start},
				{"keysym":"space", "state":console.Control_L, "function":self.timer.stop},
				{"keysym":"BackSpace", "state":console.Control_L, "function":self.timer.reset},
				{"keysym":"Tab", "state":console.Control_L, "function":self.timer.set_task}]


	def insert(self):
		inp = self.entry.get()
		self.board[self.indices] = inp
		self.Labels[self.indices].config(text=inp)
		self.entry.delete(0, tk.END)			
		self.board = loop_list(self.saver.load())


	def delete(self):
		self.board[self.indices] = 0
		self.Labels[self.indices].config(text=0)	
		self.board = loop_list(self.saver.load())
	

	def save(self):
		self.saver.save(self.board)


class Timer(tk.Frame):
	
	def __init__(self, master, task=""):		
		self.master = master
		self.range = 60 * 3 
		
		super().__init__(master)
		self.display = tk.Label(self, font=("Helvetica", 20))
		self.task_displayer = tk.Label(self, text= task)

		self.display.grid()
		self.task_displayer.grid()

		self.set_default()		



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
		self.main()

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









        



