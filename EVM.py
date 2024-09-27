from tkinter import*
root=Tk()
root.title("EVM")
root.geometry("500x500")

v1=0
v2=0

def vote1():
    global v1
    v1=v1+1
    print("volue of v1",v1)
def vote2():
    global v2
    v2=v2+1
    print("value of v2",v2)


def Result():
    if(v1>v2):
        Label(root,text="winner:party-1",height=2,width=20).grid(row=1,column=1)
    elif(v2>v1):
        Label(root,text="winner:party-1",height=2,width=20).grid(row=2,column=1)
    elif(v1==v2):
        Label(root,text="Result Tie",heigh=2,width=20).grid(row=3,column=3) 
        
    btn1.config(state="disabled")
    btn2.config(state="disabled")
    
    
Label(root,text="party-1",height=2,width=10).grid(row=1,columns=1)
btn1=Button(root,text="vote",command=vote1).grid(row=1,column=2)


Label(root,text="party-2",height=2,width=10).grid(row=1,column=1)
btn2=Button(root,text="vote",command=vote2).grid(row=2,column=1)

btn3=Button(root,text="Result",command=Result).grid(row=3,column=3)
w=Entry(root,text="Enter name")
w.grid(row=5,column=3)

val=w.get()
print("value in entry:")


