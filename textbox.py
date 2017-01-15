import Tkinter as tk

root = tk.Tk()

###############################################################################
##############Instructions#####################################################
###############################################################################
instructions = "Select and analyze a theme from 'Hamlet' by William Shakespeare. How does the use of literary devices support the theme you have selected?"

msg = tk.Message(root, text = instructions)
msg.config(font=('bold'), width=700, pady=10)
msg.grid(row=0, column =1, rowspan=2)

###############################################################################
##############TEXTBOX##########################################################
###############################################################################
def enter(event):
    # replace with update checklist function
    print("update checklist") 

h = 40
w = 100

textPanel = tk.PanedWindow(orient=tk.HORIZONTAL)
textPanel.config(bg = 'black')
textPanel.grid(row = 2, column = 1, rowspan = h)

S = tk.Scrollbar(root)
T = tk.Text(textPanel, height=h, width=w, pady=10)
# S.pack(side=RIGHT, fill=Y)
# T.pack(side=LEFT, fill=Y)
S.grid(row =2, column =2, rowspan=h)
# T.grid(row=2, column =1, rowspan=h)
textPanel.add(T)

T.bind('<Return>', enter)

S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tk.END, quote)

###############################################################################
##############CHECKLIST########################################################
###############################################################################
terms = ['Hamlet', 'nobler', 'suffer', 'slings', 'arrows', 'fortunes']

listPanel = tk.PanedWindow(orient=tk.VERTICAL)
listPanel.config(bg = 'black')

checklistFrame = tk.Frame(listPanel)

# listPanel.grid(row = 2, column = 4, rowspan = h)
textPanel.add(listPanel)
listPanel.add(checklistFrame)
def checked(event, x):
    print(x)
    # replace with update article lists panel function
    if x is 0:
    	print('checked')
    if x is 1:
    	print('unchecked')

for term in terms:
	var = tk.IntVar()
	item = tk.Checkbutton(checklistFrame, text=term, variable=var)
	x = var
	# checklistFrame.add(item)
	item.grid(row=terms.index(term) + 2, column =4, sticky=tk.W)

	def checkedHelp(event, var=var): 
		return checked(event, var.get())
	
	item.bind('<Button-1>', checkedHelp)

###############################################################################
##############READING RESOURCES################################################
###############################################################################

top = tk.Label(listPanel, text="Reading Resources")
listPanel.add(top)

bottom = tk.Label(listPanel, text="Article Preview")
listPanel.add(bottom)


tk.mainloop()



























