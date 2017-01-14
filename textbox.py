from Tkinter import *

root = Tk()

h = 40
w = 100
instructions = "Select and analyze a theme from 'Hamlet' by William Shakespeare. How does the use of literary devices support the theme you have selected?"
# msg = Label(root, justify=LEFT, pady=10, text=instructions)
msg = Message(root, text = instructions)
msg.config(font=('bold'), width=700, pady=10)
msg.grid(row=0, column =1, rowspan=2)

# S = Scrollbar(root)
T = Text(root, height=h, width=w, pady=10)
# S.pack(side=RIGHT, fill=Y)
# T.pack(side=LEFT, fill=Y)
# S.grid(row =2, column =2, rowspan=h)
T.grid(row=2, column =1, rowspan=h)

# S.config(command=T.yview)
# T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(END, quote)

# master = Tk()
var1 = IntVar()
Checkbutton(root, text="male", variable=var1).grid(row=2, column =4, sticky=W)
var2 = IntVar()
Checkbutton(root, text="female", variable=var2).grid(row=3, column =4, sticky=W)
var3 = IntVar()
Checkbutton(root, text="hi", variable=var3).grid(row=4, column =4, sticky=W)

mainloop()