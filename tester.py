
from importlib import reload 

def reloader(module):
	return lambda : reload(module)