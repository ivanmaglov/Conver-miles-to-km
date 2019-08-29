from tkinter import *

root=Tk()
root.title("Convert miles to km")
root.resizable(0,0)

def Convert():
    kilometer=float(varmile.get()/0.62137)
    convert=str('%.2f' % (kilometer)+" kilometers")
    label2.configure(text=convert)

varmile=DoubleVar()

label1=Label(root,text="Convert miles to km", padx=12,pady=12,bd=12,fg="#000000",
            font=('arial',30,'bold'), bg='light goldenrod yellow',relief='raise',width=25,height=3)
label1.pack()

slider=Scale(root,variable=varmile, from_=1, to=300, length=600,tickinterval=20,width=25,orient=HORIZONTAL)
slider.pack()

label2=Label(root, padx=16,pady=16,bd=16,fg="#000000",font=('arial',30,'bold'), bg='light goldenrod yellow',relief='sunk',width=25,height=3)
label2.pack()

label3=Label(root,text="  ")
label3.pack()

btn=Button(root,text="Convert miles to kilometers",padx=12, pady=12,bd=16,width=25,font=('arial',20,'bold'), command=Convert)
btn.pack(anchor=CENTER)

root.mainloop()
