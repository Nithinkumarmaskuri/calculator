from tkinter import*

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
                
            except Exception as e:
                print(e)
                value = "error"
                
        scvalue.set(value)
        screen.update()   
        
    elif text == "C":
        scvalue.set("")
        screen.update()
        
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()    
        
cric = Tk()
cric.geometry("500x900")
cric.title(" NITHIN'S CALCULATOR:") 
#cric.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(cric , textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


f= Frame(cric , background="grey")
b= Button(f, text="C", padx=8, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="%", padx=8, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="AC", padx=8, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=8, pady=8)
b.bind("<Button-1>",click)

b= Button(f, text="/", padx=8, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

f.pack()

f= Frame(cric , background="grey")
b= Button(f, text="7", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="8", padx=12, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="9", padx=12, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="*", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

f.pack()

f= Frame(cric , background="grey")
b= Button(f, text="4", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="5", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="6", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="-", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=12, pady=10)
b.bind("<Button-1>",click)

f.pack()

f= Frame(cric , background="grey")
b= Button(f, text="1", padx=13, pady=7, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="2", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="3", padx=13, pady=10, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="+", padx=13, pady=7, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

f.pack()

f= Frame(cric , background="grey")
b= Button(f, text="00", padx=11, pady=7, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="0", padx=13, pady=8, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text=".", padx=13, pady=8, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(f, text="=", padx=11, pady=7, font="lucida 35 bold")
b.pack(side = LEFT , padx=10, pady=10)
b.bind("<Button-1>",click)

f.pack()


                 
                  
                    
cric.mainloop()
