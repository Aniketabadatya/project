from tkinter import *
import os

def restart():
	os.system("Restart /r /t 1")

def restart_time():
	os.system("Restart_Time /r /t 20")

def logout():
	os.system("Shutdown -l")

def shutdown():
	os.system("Shutdown /s /t 1")

	
st=Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="red")
 
r = Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")
r.place(x=150,y=60,height=50,width=200)

rt = Button(st,text="Restart_Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")
rt.place(x=150,y=170,height=50,width=200)

lg = Button(st,text="Log-out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")
lg.place(x=150,y=270,height=50,width=200)

ST = Button(st,text="Shutdown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus")
ST.place(x=150,y=370,height=50,width=200)

st.mainloop()















#%%

#%%
