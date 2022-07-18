from tkinker import *
from tkinker.ttk import *

from time import strftime

root = tk()
root.title = root('clock')

def time():
	string = strftime('%H:%M:%S p%')
	label.config(text=string)
	label.after(1000 ,time)

label =	label(root, font =('sans', 80) background = 'black', foreground = 'cyan')
label.pack(anchor= center)

time()

mainloop()