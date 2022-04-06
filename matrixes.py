from tkinter import *
from tkinter import ttk
import threading
from tkinter import messagebox
from matplotlib.pyplot import text
import time


def give_val(a1,b1,a2,b2,a3,b3,write,i):
    write[i]=(a1*b1)+(a2*b2)+(a3*b3)
    print(f"({a1}*{b1})+({a2}*{b2})+({a3}*{b3})={write[i]}")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()



ttk.Label(frm, text="Matrix Multiplier").grid(column=0, row=0)
entryA11=Entry(frm,text="1,1A")
entryA11.grid(column=1,row=1)
entryA12=Entry(frm,text="1,2A")
entryA12.grid(column=2,row=1)
entryA13=Entry(frm,text="1,3A")
entryA13.grid(column=3,row=1)
entryA21=Entry(frm,text="2,1A")
entryA21.grid(column=1,row=2)
entryA22=Entry(frm,text="2,2A")
entryA22.grid(column=2,row=2)
entryA23=Entry(frm,text="2,3A")
entryA23.grid(column=3,row=2)
entryA31=Entry(frm,text="3,1A")
entryA31.grid(column=1,row=3)
entryA32=Entry(frm,text="3,2A")
entryA32.grid(column=2,row=3)
entryA33=Entry(frm,text="3,3A")
entryA33.grid(column=3,row=3)

entryB11=Entry(frm,text="1,1B")
entryB11.grid(column=6,row=1)
entryB12=Entry(frm,text="1,2B")
entryB12.grid(column=7,row=1)
entryB13=Entry(frm,text="1,3B")
entryB13.grid(column=8,row=1)
entryB21=Entry(frm,text="2,1B")
entryB21.grid(column=6,row=2)
entryB22=Entry(frm,text="2,2B")
entryB22.grid(column=7,row=2)
entryB23=Entry(frm,text="2,3B")
entryB23.grid(column=8,row=2)
entryB31=Entry(frm,text="3,1B")
entryB31.grid(column=6,row=3)
entryB32=Entry(frm,text="3,B")
entryB32.grid(column=7,row=3)
entryB33=Entry(frm,text="3,3B")
entryB33.grid(column=8,row=3)



def click():
    A11=float(entryA11.get())
    A12=float(entryA12.get())
    A13=float(entryA13.get())
    A21=float(entryA21.get())
    A22=float(entryA22.get())
    A23=float(entryA23.get())
    A31=float(entryA31.get())
    A32=float(entryA32.get())
    A33=float(entryA33.get())

    print(f"A=\n{A11} {A12} {A13}\n{A21} {A22} {A23}\n{A31} {A32} {A33}\n")



    B11=float(entryB11.get())
    B12=float(entryB12.get())
    B13=float(entryB13.get())
    B21=float(entryB21.get())
    B22=float(entryB22.get())
    B23=float(entryB23.get())
    B31=float(entryB31.get())
    B32=float(entryB32.get())
    B33=float(entryB33.get())

    print(f"B=\n{B11} {B12} {B13}\n{B21} {B22} {B23}\n{B31} {B32} {B33}\n")

    C=[0,0,0,0,0,0,0,0,0]
    C11=threading.Thread(target=give_val(A11,B11,A12,B21,A13,B31,C,0))
    C12=threading.Thread(target=give_val(A11,B12,A12,B22,A13,B32,C,1))
    C13=threading.Thread(target=give_val(A11,B13,A12,B23,A13,B33,C,2))

    C21=threading.Thread(target=give_val(A21,B11,A22,B21,A23,B31,C,3))
    C22=threading.Thread(target=give_val(A21,B12,A22,B22,A23,B32,C,4))
    C23=threading.Thread(target=give_val(A21,B13,A22,B23,A23,B33,C,5))


    C31=threading.Thread(target=give_val(A31,B11,A32,B21,A33,B31,C,6))
    C32=threading.Thread(target=give_val(A31,B12,A32,B22,A33,B32,C,7))
    C33=threading.Thread(target=give_val(A31,B13,A32,B23,A33,B33,C,8))

    C11.start()
    C12.start()
    C13.start()
    C21.start()
    C22.start()
    C23.start()
    C31.start()
    C32.start()
    C33.start()

    while C11.is_alive() or C12.is_alive() or C13.is_alive() or C21.is_alive() or C22.is_alive() or C23.is_alive() or C31.is_alive() or C32.is_alive() or C33.is_alive():
        time.sleep(0.1)



    print(f"\n{C[0]} {C[1]} {C[2]}\n{C[3]} {C[4]} {C[5]}\n{C[6]} {C[7]} {C[8]}\n")
    messagebox.showinfo("Answer",f"\n{C[0]}\t{C[1]}\t{C[2]}\n{C[3]}\t{C[4]}\t{C[5]}\n{C[6]}\t{C[7]}\t{C[8]}\n")




entryAx=Button(frm,text="X",command=click).grid(column=5,row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()


