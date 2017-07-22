from Tkinter import*
fup=Frame()
quantity=StringVar()
label1=Label(fup,text='quantity',width=8)
entry1=Entry(fup,textvariable=quantity,width=20)
label1.grid(row=1,column=1)
entry1.grid(row=1,column=2)

f2=Frame()

bt1=Button(f2,text='reset')
bt2=Button(f2,text='shuru')
bt3=Button(f2,text='duru.txt')

bt4=Button(f2,text='shengcheng.pdf')

f3=Frame()
yulan=StringVar()
label1=Label(fup,text='yulan',width=8)
entry1=Entry(fup,textvariable=yulan,width=20)
label1.grid(row=3,column=1)
entry1.grid(row=3,column=2)


bt1.grid(row=1,column=1)
bt2.grid(row=1,column=2)
bt3.grid(row=2,column=1)
bt4.grid(row=2,column=2)

fup.pack()
f2.pack()
f3.pack()
mainloop()
