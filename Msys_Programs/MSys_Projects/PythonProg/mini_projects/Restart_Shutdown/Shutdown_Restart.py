from tkinter import  *
import os

def Restart():
    os.system("shutdown /r /t 1")

def Restart_Time():
    os.system("shutdown /r /t 20")
def LOG_OUT():
    os.system("shutdown -1")
def ShoutDown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")
r_button = Button(st, text='Restart' ,font=('Time new Roman', 30, 'bold'),relief=RAISED, cursor='plus', command=Restart)
r_button.place(x=150,y=60,height=50,width=200)

r_button = Button(st, text='Restart_Time' ,font=('Time new Roman', 20, 'bold'),relief=RAISED, cursor='plus', command=Restart_Time)
r_button.place(x=150,y=170,height=50,width=200)

r_button = Button(st, text='LOG_OUT' ,font=('Time new Roman', 20, 'bold'),relief=RAISED, cursor='plus', command=LOG_OUT)
r_button.place(x=150,y=270,height=50,width=200)

r_button = Button(st, text='ShoutDown' ,font=('Time new Roman', 20, 'bold'),relief=RAISED, cursor='plus', command=ShoutDown)
r_button.place(x=150,y=370,height=50,width=200)





st.mainloop()