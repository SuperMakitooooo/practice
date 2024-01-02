from glob import glob
from PIL import Image
import tkinter 
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import converter




path = askfiledirectory()
zip = converter(path)
zip.extract()

webp_links = g(zip.extracted + "/*")
webps = [converter(link) for link in webp_links]
for webp in webps:
	webp.webp_to_jpg()

dir = converter(zip.extracted)
dir.to_pdf()





"""
class convert_to_pdf:
	"""
	data_type:
	parents = {	"parent": current_dir,	
			"zip": zip_path,
			"extracted":dirs in which webp files are,
			"converted": dirs in which jpeg files are,
			"result": dirs to which put result }
	child = {		"extracted": extracted file,
			"converted": converted file}

	#all dirs are given by paths
	
	flowchart:
	__init__: set "parents" data
	makedir: "extracted", "converted" folder 
	set_extracted_dir:
	gen_path	

	"""	

	def __init__(self=None):
		self.parents = {	"parent"	:(c_path:=askdirectory()),
				"zip"		:c_path,
				"extracted"	:c_path + "/webp",
				"converted"	:c_path + "/jpeg",
				"result"	:c_path + "/result"}  

	def run(self):
		self.parents = {	"parent"	:(c_path:=askdirectory()),
				"zip"		:askdirectory(),
				"extracted"	:c_path + "/webp",
				"converted"	:c_path + "/jpeg",
				"result"	:c_path + "/result"} 
		
		self.makedirs()
		converter.unpack()
		self.set_extracted_dir()
		self.mainloop()
		self.to_pdf()
		to_pdf(self.parents["converted"], self.parents["parent"]+"/result.pdf")
		

		
	def makedirs(self=None):
		try:
			os.makedirs(parents["extracted"])
			os.makedirs(parents["converted"])
		except Exception as  e:
			print(e)

	def unpack(self=None):
		shutil.unpack_archive(parents["zip"], parents["extracted"])

		


	def set_extracted_dir(self=None):
		path_webp = parents["extracted"] + "/*.webp"
		path_to_convert = glob(webp)
		self.children = {		"extracted":	path_to_convert	}


	def gen_path(self, from_child, to_parent, filetype=".jpg"):
		fullname = os.path.basename(from_child)
		title = os.path.splitext(fullname)[0]
		to_child = to_parent + "/" + title + filetype
		return to_child


	def mainloop(self):
		for child_extracted in self.children["extracted"]:
			child_converted = self.gen_path(child_extracted, self.parents["converted"])
			im = Image.open(child_extracted).convert("RGB")
			im.save(child_converted)


	def to_pdf(self, dir_path, file_name):
		paths = glob(dir_path + "/*")
		images = [Image.open(path).convert("RGB") for path in paths]
		pdf = images[0].save(	dir_path + "/"+file_name, 
					save_all=True, 
					append_images=images[1:])

"""
if __name__ == "__main__":
	a = covert_to_pdf()
	

