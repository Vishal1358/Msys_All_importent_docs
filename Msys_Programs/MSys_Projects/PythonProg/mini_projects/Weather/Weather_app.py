from tkinter import *
from tkinter import ttk
import requests

# 96c86dad2277b39b5fe58626c886cd2a - API Key

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}   -- API Url

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=96c86dad2277b39b5fe58626c886cd2a").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])
    
    print(data)
    
    


# def get_weather(api_key, city):
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     parms = {
#         "q":city,
#         "appid": api_key,
#         "units": "metric"
#     }
#     response = requests.get(base_url,params=parms)
#     data = response.json()
#     return data

# def display():
#     city = city_entry


win = Tk()
win.title("Python Weather")
win.config(bg="blue")
win.geometry("570x570")
name_label = Label(win, text="Python Weather App",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name = StringVar()
com = ttk.Combobox(win,text="Python Weather App",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win, text="Weather Climate",font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win, text="",font=("Time New Roman",15))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win, text="Weather Description",font=("Time New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win, text="",font=("Time New Roman",15))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win, text="Temperature",font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win, text="",font=("Time New Roman",15))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win, text="Pressure",font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win, text="",font=("Time New Roman",15))
per_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win, text="Done",font=("Time New Roman",30,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)


win.mainloop()