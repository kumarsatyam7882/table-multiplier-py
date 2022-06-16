from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Multiply printer")
root.resizable(0,0)
root.wm_iconbitmap('multiply.ico')

var = StringVar()

def mul():
	txtResult.delete(1.0,END)
	m = var.get()
	if m.isdigit():
		m = int(m)
		for i in range(1,11):
			txtResult.insert(END, '\n\t')
			txtResult.insert(END,m,'\t','X','\t',i,'\t','=','\t',(m*i))
			txtResult.insert(END,'\n')
		return True
	else:
		messagebox.showwarning("Error","Please enter number")
		var.set("")
		return False

def Reset():
	if messagebox.askyesno("Multiplication table","Confirm if you want to reset"):
		txtResult.delete(1.0,END)
		var.set("")

def Exit():
	if messagebox.askyesno("Multiplication table","Confirm if you want to exit"):
		root.destroy()
	else:
		txtResult.delete(1.0,END)
		var.set("")

f = Frame(root, bg="black", relief=RIDGE, padx=30, pady=30)
f.grid()

lf = Frame(f, bd=7, width=400, height=500, relief=RIDGE)
lf.grid(row=0, column=0, padx=30)

rf = Frame(f, bd=7, width=400, height=500, relief=RIDGE)
rf.grid(row=0, column=1, padx=30)

titleLabel = Label(rf, text="Table", font="Ds-Digital 35 bold", bg="black", fg="cyan")
titleLabel.grid(row=0, column=0)

txtResult = Text(rf, font="arial 13 bold", bd=10, width=30, height=23)
txtResult.grid(row=1, column=0, pady=20)

title = Label(lf, text="Number", font="Ds-Digital 40 bold", bg="black", fg="cyan", width=12)
title.grid(row=0, column=0, padx=30, pady=20)

e = Entry(lf, textvariable=var, font="arial 20 bold", bd=10, justify="center")
e.grid(row=1, column=0, pady=20)

bt1 = Button(lf, text="Multiply", font="Ds-Digital 29 bold", bg="black", fg="cyan", bd=10, width=13, command=mul)
bt1.grid(row=2, column=0, pady=20)

bt2 = Button(lf, text="Reset", font="Ds-Digital 29 bold", bg="black", fg="cyan", bd=10, width=13, command=Reset)
bt2.grid(row=3, column=0, pady=20)

bt3 = Button(lf, text="Exit", font="Ds-Digital 29 bold", bg="black", fg="cyan", bd=10, width=13, command=Exit)
bt3.grid(row=4, column=0, pady=20)

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()