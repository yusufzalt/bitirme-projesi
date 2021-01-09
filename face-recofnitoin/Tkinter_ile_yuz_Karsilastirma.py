# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:31:19 2020

@author: abdul
"""

from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog
import sys
import face_recognition as fr

root=tk.Tk()
btn_Karsilastir=None
btn2_right=None
btn1_lef=None
panel=None
panel2=None
HEIGHT,WIDTH=520,700



canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
root.title('Yüz Kariılaştırma')

title=tk.Label(root,text='Face Match',font='Helvetica 20')
title.place(x=300,y=10)



frame1=tk.Frame(root,highlightbackground='gray',highlightcolor='gray',highlightthickness=1.5,bd=10)
frame1.place(x=350,y=50,width=690,height=300,anchor='n')


    

def openfn():
    filename=filedialog.askopenfilename(title='open')
    return filename
frame4=tk.Frame(root,highlightbackground='gray',highlightcolor='gray',highlightthickness=1.5,bd=10)
frame4.place(x=10,y=360,width=690,height=100)


r_image=[]
def right_open_image():
    
    x=openfn()
    img=Image.open(x)
    img=img.resize((200,200),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    global panel
    panel=tk.Label(frame3,image=img)
    panel.image=img
    panel.pack()
    btn_Karsilastir.config(state='normal')
    btn2_right.config(state="disabled")
    r_image.append(x)
    
    
   
l_image=[]
def left_open_image():    
    y=openfn()
    img=Image.open(y)
    img=img.resize((200,200),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    panel2=tk.Label(frame2,image=img)
    panel2.image=img
    panel2.pack()
    btn2_right.config(state='normal')
    btn1_lef.config(state='disabled')
    l_image.append(y)
    
    


def face_much(left_image,right_image):
    left_image=fr.load_image_file(left_image)
    left_face_encoding=fr.face_encodings(left_image)[0]
    
    right_image=fr.load_image_file(right_image)
    right_face_encoding=fr.face_encodings(right_image)[0]
    
    known_encoding=[right_face_encoding]
    result=fr.compare_faces([left_face_encoding], right_face_encoding)
    face_destances=fr.face_distance(left_face_encoding, known_encoding)
    
    btn1_lef.config(state="disabled")
    btn2_right.config(state="disabled")
    btn_Karsilastir.config(state='disabled')
    
    if result[0]:
        rst='ayni kisidir {} %'.format(face_destances*100)
    else:
        rst='ayni kisi olmama ihtimali {} %'.format(face_destances*100)
        
    return rst

def images():
    l_x=l_image
    l_x=''.join(map(str, l_x))
    
    r_x=r_image
    r_x=''.join(map(str,r_x))
    
    face_much(l_x,r_x)
    print_result.configure(text=face_much(l_x,r_x))
 

def Cikis():
    root.destroy()
    sys.exit()

def frame_2():
    global frame2
    frame2=tk.Frame(frame1,highlightbackground='gray',highlightcolor='gray',highlightthickness=1.5,bd=10)
    frame2.place(x=10,y=70,width=200,height=200)

def frame_3():
    global frame3
    frame3=tk.Frame(frame1,highlightbackground='gray',highlightcolor='gray',highlightthickness=1.5,bd=10)
    frame3.place(x=433,y=70,width=200,height=200)
    
btn1_lef=tk.Button(frame1,text='Sol Resim Yukle',font='Helvetica 15',bg='green',fg='white',command=left_open_image)
btn1_lef.place(x=110,anchor='n')

btn2_right=tk.Button(frame1,text='Sag Resim Yukle',font='Helvetica 15',bg='green',state="disabled",fg='white',command=right_open_image)
btn2_right.place(x=540,anchor='n')
                        
btn_Karsilastir=tk.Button(frame1,text='Karsilastir',font='Helvetica 15',bg='green',state="disabled",fg='white',command=images)
btn_Karsilastir.pack(anchor='n')

btn_cikis=tk.Button(root,text='Cikis Yap',font='Helvetica 15',bg='green',fg='white',command=Cikis)
btn_cikis.place(x=50,y=470)


print_result=tk.Label(frame4, font='Helvetica 20')
print_result.place(x=0,y=10)



def yenile():
    frame2.place_forget()
    frame3.place_forget()
    print_result.config(text='')   
    frame_2()
    frame_3()
    r_image.clear()
    l_image.clear()
    btn1_lef.config(state="normal")
    btn_Karsilastir.config(state='disabled')
    
       
btn_yenile=tk.Button(root,text='Sayfayi Yenile',font='Helvetica 15',bg='green',fg='white',command=yenile)
btn_yenile.place(x=200,y=470)

frame_2()
frame_3()
root.mainloop()