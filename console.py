import tkinter as tk
import curses

class Any(object):
	def __eq__(self, other):
		return True

	def __repr__(self):
		return "'Any'"

	def __gt__(self):
		pass


	
	
	


class patterns(object):
	Any = Any()
	Control_R = 262148
	Control_L = 1028
	Shift  = 1
	Alt_L = 131072
	Alt_R = 393216	

	


	def __init__(self, array=[]):
		self.body = array	


	def __getitem__(self, index_tuple):
		print(index_tuple)
		f = self.search({"keysym": index_tuple[0], "state":index_tuple[1]})
		return f


	def search(self, insert):
		for pattern in self.body:
			function = pattern["function"]		

			sym = (pattern["keysym"] == insert["keysym"])
			state = (pattern["state"] == insert["state"])

			if sym & state:
				function = pattern["function"]
				break
			else :
				function = self.empty
		return function		


	def empty(self):
		return


class console(patterns):
	body = [{"keysym":"m", "state":"0", "function":print}]			
	


	def __init__(self):
		super().__init__()


	def run(self, key):
		print(self.body)
		function = self[key.keysym, key.state]
		return function()


			




class patterns_for_curses(object):
	body = {curses.KEY_UP:"up"}

	def __init__(self, array=[]):
		self.body = array


	def __getitem__(self, name):
		return self[name]	



	def empty(self):
		return

keys =	{'ERR': -1, 
	'OK': 0, 
	'BUTTON1_PRESSED': 2, 
	'BUTTON1_RELEASED': 1, 
	'BUTTON1_CLICKED': 4, 
	'BUTTON1_DOUBLE_CLICKED': 8, 
	'BUTTON1_TRIPLE_CLICKED': 16, 
	'BUTTON2_PRESSED': 64, 
	'BUTTON2_RELEASED': 32, 
	'BUTTON2_CLICKED': 128, 
	'BUTTON2_DOUBLE_CLICKED': 256, 
	'BUTTON2_TRIPLE_CLICKED': 512, 
	'BUTTON3_PRESSED': 2048, 
	'BUTTON3_RELEASED': 1024, 
	'BUTTON3_CLICKED': 4096, 
	'BUTTON3_DOUBLE_CLICKED': 8192, 
	'BUTTON3_TRIPLE_CLICKED': 16384, 
	'BUTTON4_PRESSED': 65536, 
	'BUTTON4_RELEASED': 32768, 
	'BUTTON4_CLICKED': 131072, 
	'BUTTON4_DOUBLE_CLICKED': 262144, 
	'BUTTON4_TRIPLE_CLICKED': 524288, 
	'BUTTON5_PRESSED': 2097152, 
	'BUTTON5_RELEASED': 1048576, 
	'BUTTON5_CLICKED': 4194304, 
	'BUTTON5_DOUBLE_CLICKED': 8388608, 
	'BUTTON5_TRIPLE_CLICKED': 16777216, 
	'BUTTON_SHIFT': 67108864, 
	'BUTTON_CTRL': 134217728, 
	'BUTTON_ALT': 268435456, 
	'ALL_MOUSE_EVENTS': 536870911, 
	'REPORT_MOUSE_POSITION': 536870912, 
	'KEY_BREAK': 257, 
	'KEY_DOWN': 258, 
	'KEY_UP': 259, 
	'KEY_LEFT': 260, 
	'KEY_RIGHT': 261, 
	'KEY_HOME': 262, 
	'KEY_BACKSPACE': 263, 
	'KEY_F0': 264, 
	'KEY_F1': 265, 
	'KEY_F2': 266, 
	'KEY_F3': 267, 
	'KEY_F4': 268, 
	'KEY_F5': 269, 
	'KEY_F6': 270, 
	'KEY_F7': 271, 
	'KEY_F8': 272, 
	'KEY_F9': 273, 
	'KEY_F10': 274, 
	'KEY_F11': 275, 
	'KEY_F12': 276, 
	'KEY_F13': 277, 
	'KEY_F14': 278, 
	'KEY_F15': 279, 
	'KEY_F16': 280, 
	'KEY_F17': 281, 
	'KEY_F18': 282, 
	'KEY_F19': 283, 
	'KEY_F20': 284, 
	'KEY_F21': 285, 
	'KEY_F22': 286, 
	'KEY_F23': 287, 
	'KEY_F24': 288, 
	'KEY_F25': 289, 
	'KEY_F26': 290, 
	'KEY_F27': 291, 
	'KEY_F28': 292, 
	'KEY_F29': 293, 
	'KEY_F30': 294, 
	'KEY_F31': 295, 
	'KEY_F32': 296, 
	'KEY_F33': 297, 
	'KEY_F34': 298, 
	'KEY_F35': 299, 
	'KEY_F36': 300, 
	'KEY_F37': 301, 
	'KEY_F38': 302, 
	'KEY_F39': 303, 
	'KEY_F40': 304, 
	'KEY_F41': 305, 
	'KEY_F42': 306, 
	'KEY_F43': 307, 
	'KEY_F44': 308, 
	'KEY_F45': 309, 
	'KEY_F46': 310, 
	'KEY_F47': 311, 
	'KEY_F48': 312, 
	'KEY_F49': 313, 
	'KEY_F50': 314, 
	'KEY_F51': 315, 
	'KEY_F52': 316, 
	'KEY_F53': 317, 
	'KEY_F54': 318, 
	'KEY_F55': 319, 
	'KEY_F56': 320, 
	'KEY_F57': 321, 
	'KEY_F58': 322, 
	'KEY_F59': 323, 
	'KEY_F60': 324, 
	'KEY_F61': 325, 
	'KEY_F62': 326, 
	'KEY_F63': 327, 
	'KEY_DL': 328, 
	'KEY_IL': 329, 
	'KEY_DC': 330, 
	'KEY_IC': 331, 
	'KEY_EIC': 332, 
	'KEY_CLEAR': 333, 
	'KEY_EOS': 334, 
	'KEY_EOL': 335, 
	'KEY_SF': 336, 
	'KEY_SR': 337, 
	'KEY_NPAGE': 338, 
	'KEY_PPAGE': 339, 
	'KEY_STAB': 340, 
	'KEY_CTAB': 341, 
	'KEY_CATAB': 342, 
	'KEY_ENTER': 343, 
	'KEY_SRESET': 344, 
	'KEY_RESET': 345, 
	'KEY_PRINT': 346, 
	'KEY_LL': 347, 
	'KEY_ABORT': 348, 
	'KEY_SHELP': 349, 
	'KEY_LHELP': 350, 
	'KEY_BTAB': 351, 
	'KEY_BEG': 352, 
	'KEY_CANCEL': 353, 
	'KEY_CLOSE': 354, 
	'KEY_COMMAND': 355, 
	'KEY_COPY': 356, 
	'KEY_CREATE': 357, 
	'KEY_END': 358, 
	'KEY_EXIT': 359, 
	'KEY_FIND': 360, 
	'KEY_HELP': 361, 
	'KEY_MARK': 362, 
	'KEY_MESSAGE': 363, 
	'KEY_MOVE': 364, 
	'KEY_NEXT': 365, 
	'KEY_OPEN': 366, 
	'KEY_OPTIONS': 367, 
	'KEY_PREVIOUS': 368, 
	'KEY_REDO': 369, 
	'KEY_REFERENCE': 370, 
	'KEY_REFRESH': 371, 
	'KEY_REPLACE': 372, 
	'KEY_RESTART': 373, 
	'KEY_RESUME': 374, 
	'KEY_SAVE': 375, 
	'KEY_SBEG': 376, 
	'KEY_SCANCEL': 377, 
	'KEY_SCOMMAND': 378, 
	'KEY_SCOPY': 379, 
	'KEY_SCREATE': 380, 
	'KEY_SDC': 381, 
	'KEY_SDL': 382, 
	'KEY_SELECT': 383, 
	'KEY_SEND': 384, 
	'KEY_SEOL': 385, 
	'KEY_SEXIT': 386, 
	'KEY_SFIND': 387, 
	'KEY_SHOME': 388, 
	'KEY_SIC': 389, 
	'KEY_SLEFT': 391, 
	'KEY_SMESSAGE': 392, 
	'KEY_SMOVE': 393, 
	'KEY_SNEXT': 394, 
	'KEY_SOPTIONS': 395, 
	'KEY_SPREVIOUS': 396, 
	'KEY_SPRINT': 397, 
	'KEY_SREDO': 398, 
	'KEY_SREPLACE': 399, 
	'KEY_SRIGHT': 400, 
	'KEY_SRSUME': 401, 
	'KEY_SSAVE': 402, 
	'KEY_SSUSPEND': 403, 
	'KEY_SUNDO': 404, 
	'KEY_SUSPEND': 405, 
	'KEY_UNDO': 406, 
	'ALT_0': 407, 
	'ALT_1': 408, 
	'ALT_2': 409, 
	'ALT_3': 410, 
	'ALT_4': 411, 
	'ALT_5': 412, 
	'ALT_6': 413, 
	'ALT_7': 414, 
	'ALT_8': 415, 
	'ALT_9': 416, 
	'ALT_A': 417, 
	'ALT_B': 418, 
	'ALT_C': 419, 
	'ALT_D': 420, 
	'ALT_E': 421, 
	'ALT_F': 422, 
	'ALT_G': 423, 
	'ALT_H': 424, 
	'ALT_I': 425, 
	'ALT_J': 426, 
	'ALT_K': 427, 
	'ALT_L': 428, 
	'ALT_M': 429, 
	'ALT_N': 430, 
	'ALT_O': 431, 
	'ALT_P': 432, 
	'ALT_Q': 433, 
	'ALT_R': 434, 
	'ALT_S': 435, 
	'ALT_T': 436, 
	'ALT_U': 437, 
	'ALT_V': 438, 
	'ALT_W': 439, 
	'ALT_X': 440, 
	'ALT_Y': 441, 
	'ALT_Z': 442, 
	'CTL_LEFT': 443, 
	'CTL_RIGHT': 444, 
	'CTL_PGUP': 445, 
	'CTL_PGDN': 446, 
	'CTL_HOME': 447, 
	'CTL_END': 448, 
	'KEY_A1': 449, 
	'KEY_A2': 450, 
	'KEY_A3': 451, 
	'KEY_B1': 452, 
	'KEY_B2': 453, 
	'KEY_B3': 454, 
	'KEY_C1': 455, 
	'KEY_C2': 456, 
	'KEY_C3': 457, 
	'PADSLASH': 458, 
	'PADENTER': 459, 
	'CTL_PADENTER': 460, 
	'ALT_PADENTER': 461, 
	'PADSTOP': 462, 
	'PADSTAR': 463, 
	'PADMINUS': 464, 
	'PADPLUS': 465, 
	'CTL_PADSTOP': 466, 
	'CTL_PADCENTER': 467, 
	'CTL_PADPLUS': 468, 
	'CTL_PADMINUS': 469, 
	'CTL_PADSLASH': 470, 
	'CTL_PADSTAR': 471, 
	'ALT_PADPLUS': 472, 
	'ALT_PADMINUS': 473, 
	'ALT_PADSLASH': 474, 
	'ALT_PADSTAR': 475, 
	'ALT_PADSTOP': 476, 
	'CTL_INS': 477, 
	'ALT_DEL': 478, 
	'ALT_INS': 479, 
	'CTL_UP': 480, 
	'CTL_DOWN': 481, 
	'CTL_TAB': 482, 
	'ALT_TAB': 483, 
	'ALT_MINUS': 484, 
	'ALT_EQUAL': 485, 
	'ALT_HOME': 486, 
	'ALT_PGUP': 487, 
	'ALT_PGDN': 488, 
	'ALT_END': 489, 
	'ALT_UP': 490, 
	'ALT_DOWN': 491, 
	'ALT_RIGHT': 492, 
	'ALT_LEFT': 493, 
	'ALT_ENTER': 494, 
	'ALT_ESC': 495, 
	'ALT_BQUOTE': 496, 
	'ALT_LBRACKET': 497, 
	'ALT_RBRACKET': 498, 
	'ALT_SEMICOLON': 499, 
	'ALT_FQUOTE': 500, 
	'ALT_COMMA': 501, 
	'ALT_STOP': 502, 
	'ALT_FSLASH': 503, 
	'ALT_BKSP': 504, 
	'CTL_BKSP': 505, 
	'PAD0': 506, 
	'CTL_PAD0': 507, 
	'CTL_PAD1': 508, 
	'CTL_PAD2': 509, 
	'CTL_PAD3': 510, 
	'CTL_PAD4': 511, 
	'CTL_PAD5': 512, 
	'CTL_PAD6': 513, 
	'CTL_PAD7': 514, 
	'CTL_PAD8': 515, 
	'CTL_PAD9': 516, 
	'ALT_PAD0': 517, 
	'ALT_PAD1': 518, 
	'ALT_PAD2': 519, 
	'ALT_PAD3': 520, 
	'ALT_PAD4': 521, 
	'ALT_PAD5': 522, 
	'ALT_PAD6': 523, 
	'ALT_PAD7': 524, 
	'ALT_PAD8': 525, 
	'ALT_PAD9': 526, 
	'CTL_DEL': 527, 
	'ALT_BSLASH': 528, 
	'CTL_ENTER': 529, 
	'SHF_PADENTER': 530, 
	'SHF_PADSLASH': 531, 
	'SHF_PADSTAR': 532, 
	'SHF_PADPLUS': 533, 
	'SHF_PADMINUS': 534, 
	'SHF_UP': 535, 
	'SHF_DOWN': 536, 
	'SHF_IC': 537, 
	'SHF_DC': 538, 
	'KEY_MOUSE': 539, 
	'KEY_SHIFT_L': 540, 
	'KEY_SHIFT_R': 541, 
	'KEY_CONTROL_L': 542, 
	'KEY_CONTROL_R': 543, 
	'KEY_ALT_L': 544, 
	'KEY_ALT_R': 545, 
	'KEY_RESIZE': 546, 
	'KEY_SUP': 547, 
	'KEY_MIN': 257, 
	'KEY_MAX': 548}

