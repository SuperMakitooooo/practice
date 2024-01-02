from glob import glob
from PIL import Image
import tkinter 
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import shutil
import os
from pprint import pprint as pp
import re
import pathlib

#set parent directory by user's setting


class converter:
	def __init__(self, path):
		self.path = path
		self.Path = pathlib.PurePath(path)
		self.fullpath = str(self.Path)
		self.stem = self.Path.stem
		self.parent = self.Path.parent.__str__()
		

	def extract(self):
		shutil.unpack_archive(self.fullpath, self.parent +"/"+ self.stem)
		self.extracted = self.stem


	def webp_to_jpg(self):
		im = Image.open(self.fullpath).convert("RGB")
		im.save(self.Path.stem + ".jpg")
	

	def to_pdf(self, type=".jpg"):
		all_images = f"{self.fullpath}/*{type}"
		paths = glob(all_images)
		print(paths)
		images = [Image.open(path).convert("RGB") for path in paths]
		
		pdf_path = self.Path.as_posix()+ "/" + self.Path.stem + ".pdf"
		pdf = images[0].save(	pdf_path, 
					save_all=True, 
					append_images=images[1:])


if __name__ == "__main__":
	a = covert_to_pdf()
	

