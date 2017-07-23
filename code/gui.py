from Tkinter import*
root=Tk()
root.title('HumanFont')
fup=Frame()

size=StringVar()
preview=StringVar()
filename=StringVar()

label1=Label(fup,text='size:')
entry1=Entry(fup,textvariable=size,width=20)
label1.grid(row=1,column=1)
entry1.grid(row=1,column=2)

label3=Label(fup,text='filename:')
entey3=Entry(fup,text=filename,width=20)
label3.grid(row=2,column=1)
entey3.grid(row=2,column=2)


bt4=Button(fup,text='OutputPDF')
bt3=Button(fup,text='Input')




bt3.grid(row=2,column=3)
bt4.grid(row=4,column=2)


fup.pack()
mainloop()