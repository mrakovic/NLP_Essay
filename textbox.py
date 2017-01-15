import Tkinter as tk

root = tk.Tk()

h = 40
w = 100
instructions = "Select and analyze a theme from 'Hamlet' by William Shakespeare. How does the use of literary devices support the theme you have selected?"
# msg = Label(root, justify=LEFT, pady=10, text=instructions)
def enter(event):
    # replace with update checklist function
    print("update checklist") 
def bye(event):
    print("bye")

def checked(event, x):
    print(x)
    # replace with update article lists panel function
    if x is 0:
    	print('checked')
    if x is 1:
    	print('unchecked')

msg = tk.Message(root, text = instructions)
msg.config(font=('bold'), width=700, pady=10)
msg.grid(row=0, column =1, rowspan=2)

S = tk.Scrollbar(root)
T = tk.Text(root, height=h, width=w, pady=10)
# S.pack(side=RIGHT, fill=Y)
# T.pack(side=LEFT, fill=Y)
S.grid(row =2, column =2, rowspan=h)
T.grid(row=2, column =1, rowspan=h)

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

terms = ['Hamlet', 'nobler', 'suffer', 'slings', 'arrows', 'fortunes']
# master = Tk()
# var1 = tk.IntVar()
# check1 = tk.Checkbutton(root, text="Hamlet", variable=var1)
# check1.grid(row=2, column =4, sticky=tk.W)
# check1.bind('<Button-1>', hello)

for term in terms:
	var = tk.IntVar()
	item = tk.Checkbutton(root, text=term, variable=var)
	x = var
	item.grid(row=terms.index(term) + 2, column =4, sticky=tk.W)

	def checkedHelp(event, var=var): 
		return checked(event, var.get())
	
	item.bind('<Button-1>', checkedHelp)

tk.mainloop()