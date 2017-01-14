import Tkinter as tk

root = tk.Tk()

h = 40
w = 100
instructions = "Select and analyze a theme from 'Hamlet' by William Shakespeare. How does the use of literary devices support the theme you have selected?"
# msg = Label(root, justify=LEFT, pady=10, text=instructions)
msg = tk.Message(root, text = instructions)
msg.config(font=('bold'), width=700, pady=10)
msg.grid(row=0, column =1, rowspan=2)

S = tk.Scrollbar(root)
T = tk.Text(root, height=h, width=w, pady=10)
# S.pack(side=RIGHT, fill=Y)
# T.pack(side=LEFT, fill=Y)
S.grid(row =2, column =2, rowspan=h)
T.grid(row=2, column =1, rowspan=h)

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

# master = Tk()
var1 = tk.IntVar()
tk.Checkbutton(root, text="Hamlet", variable=var1).grid(row=2, column =4, sticky=tk.W)
var2 = tk.IntVar()
tk.Checkbutton(root, text="nobler", variable=var2).grid(row=3, column =4, sticky=tk.W)
var3 = tk.IntVar()
tk.Checkbutton(root, text="suffer", variable=var3).grid(row=4, column =4, sticky=tk.W)
var4 = tk.IntVar()
tk.Checkbutton(root, text="slings", variable=var3).grid(row=5, column =4, sticky=tk.W)
var5 = tk.IntVar()
tk.Checkbutton(root, text="arrows", variable=var3).grid(row=6, column =4, sticky=tk.W)
var6 = tk.IntVar()
tk.Checkbutton(root, text="fortune", variable=var3).grid(row=7, column =4, sticky=tk.W)


tk.mainloop()