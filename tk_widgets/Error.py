import tkinter as tk
from modules.console import console 


class Error_popup(tk.Tk):
    def __init__(self, cls):
        try:
            A = cls()
            A.mainloop()
        except Exception as e:
            super().__init__() 
            self.init(e)
            

    def init(self, error):
        self.error = error
        self.console = console()
        self.console.body += [{"keysym":"Return", "state":console.Any, "function":self.destroy}]
        self.label = tk.Label(self, text=error.__repr__())
        self.label.grid()
        
    
    
