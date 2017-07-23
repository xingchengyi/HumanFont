# -*- coding: utf-8 -*-
import core
import get_text
from Tkinter import*
root=Tk()
root.title('HumanFont')
fup=Frame()
o_button = Frame()

size=StringVar()
filename=StringVar()
outputname=StringVar()


label1=Label(fup,text='size:')
entry1=Entry(fup,textvariable=size,width=20)
label2=Label(fup,text='outputname:')
entey2=Entry(fup,textvariable=outputname)
label3=Label(fup,text='filename:')
entey3=Entry(fup,textvariable=filename,width=20)
bt_output=Button(o_button,text='OutputPDF',command = lambda: core.core(outputname.get(),get_text.get_text(str(filename.get())).decode('utf-8'),int(size.get())))


label3.grid(row=2,column=1)
entey3.grid(row=2,column=2)
label1.grid(row=1,column=1)
entry1.grid(row=1,column=2)
label2.grid(row=4,column=1)
entey2.grid(row=4,column=2)
bt_output.grid(row=1,column=1)


fup.pack()
o_button.pack()
mainloop()