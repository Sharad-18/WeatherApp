from ast import Delete
from logging import root
from msilib.schema import Icon
import tkinter as tk
from turtle import heading
from webbrowser import get
import requests
from PIL import Image,ImageTk
root=tk.Tk()
root.title("Wether App")
root.geometry("600x500")
# key-: d6cf59f79c0d8fa9185c806e129b283a
# api:- https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(wether):
    try:
        city= wether['name']
        condition=wether['weather'][0]['description']
        Temprature=wether['main']['temp']
        final_str='city:%s\ncondition:%s\nTemprature:%s'%(city,condition,Temprature)
    except:
        final_str=f'There is a problem to retrieving information from {city}'
    return final_str




def get_wether(city):
    weather_key='d6cf59f79c0d8fa9185c806e129b283a'
    url='https://api.openweathermap.org/data/2.5/weather'
    paramet_et={'appid':weather_key,'q':city,'units':'imperial'}
    respons=requests.get(url,paramet_et)
    # print(respons.json())
    wether=respons.json()

    # print(wether['name'])
    # print(wether['weather'][0]['description'])
    # print(wether['main']['temp'])

    result['text']=format_response(wether)
    icon_name=wether['weather'][0]['icon']
    






img=Image.open('./pic.png')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text='Check Wether By Using Name Of Cities',fg='red',bg='sky blue',font=('times new roman',18,'bold'))
heading_title.place(x=80,y=8)

frame_one=tk.Frame(bg_lbl,bg="sky blue",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)


txt_box=tk.Entry(frame_one,font=('times new roman',25),width=44)
txt_box.grid(row=0,column=0,sticky='w')

buto_n=tk.Button(frame_one,text='Get Weather',fg='green',font=('times new roman',18,'bold'),command=lambda:get_wether(txt_box.get()))
buto_n.grid(row=0,column=0,padx=10)


frame_two=tk.Frame(bg_lbl,bg="sky blue",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

# wether_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
# wether_icon.place(x=0.75,y=0,relwidth=1,relheight=0.5)

root.mainloop()
