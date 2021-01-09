# -*- coding: utf-8 -*-


import tkinter as tk
import cv2
import os
from PIL import Image, ImageTk
import numpy as np
from tkinter import messagebox
import face_recognition as fr

window = tk.Tk()
window.title('Face Recogniyion')
window.resizable(0,0)
window.geometry('800x600+200+60')
cap = cv2.VideoCapture(0)
img_logo = Image.open('logo1.png')
photo_logo = ImageTk.PhotoImage(img_logo)

btn_logo = tk.Button(window,image=photo_logo)
btn_logo.place(x=2,y=2)

canvas_frame = tk.Canvas(window,width = 400, height = 340)
canvas_frame.place(x=0, y=70)
def frame_live():
    #data = 'C:/Users/abdul/Documents/FaceRecogrition/Spider_Face/Image'
    data = 'data'
    myList = os.listdir(data)
    images = []
    img_names = []
    for img in myList:
        image = cv2.imread(f'{data}/{img}')
        images.append(image)
        img_names.append(os.path.splitext(img)[0].split('.')[0])
    
        
    def encod(images):
        encodList = []
        for img in images:
            
            img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            face_encod = fr.face_encodings(img_gray)[0]
            encodList.append(face_encod)
        return encodList
    
    know_encoding=encod(images)
    
        
    face_locations = []
    face_encodings = []
    face_names = []
    
    
    cap = cv2.VideoCapture(0)
    
    def Update():
        ret,frame = cap.read()
        process_this_frame = True
        s_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        g_frame = cv2.cvtColor(s_frame,cv2.COLOR_BGR2RGB)
        if process_this_frame:
            face_locations = fr.face_locations(g_frame)
            face_encodings = fr.face_encodings(g_frame,face_locations)
            
            face_names = []
            
            for face_encoding in face_encodings:
                matches = fr.compare_faces(know_encoding,face_encoding)
                name = 'Unknown'
                
                face_distence = fr.face_distance(know_encoding,face_encoding)
                best_match_index = np.argmin(face_distence)
                if matches[best_match_index]:
                    name = img_names[best_match_index]
                    
                face_names.append(name)
        process_this_frame = not process_this_frame
        
        for (top,right,bottom,left),name in zip(face_locations,face_names):
            top *=4
            right *=4
            bottom *=4
            left *=4
            
            cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
            cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,255,0),cv2.FILLED)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            
        img = Image.fromarray(frame)
        imgTk = ImageTk.PhotoImage(image = img)
        label_img = tk.Label(canvas_frame,image=imgTk)
        label_img.image = imgTk
        label_img.place(x=5,y=5)
            
        label_img.after(20,Update)
    width = 395
    height = 335
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    Update()
        
frame_live()       
    

canvas_info = tk.Canvas(window,width = 400, height = 340, bg = 'ivory')
canvas_info.place(x=400, y=70)

canvas_btn = tk.Canvas(window,width = 800, height = 180, bg = 'green')
canvas_btn.place(x=0, y=415)
def lbl_info():
    global ent_soyad
    global ent_ad
    global ent_yas
    global ent_adres
    lbl_ad = tk.Button(canvas_info,text = 'Ad       :', font = ('Algerian',15))
    lbl_ad.place(x=5,y=15)
    ent_ad = tk.Entry(canvas_info,font = ('Arial',19))
    ent_ad.place(x=105,y=15)
    
    lbl_soyad = tk.Button(canvas_info,text = 'Soyad:', font = ('Algerian',15))
    lbl_soyad.place(x=5,y=60)
    ent_soyad = tk.Entry(canvas_info,font = ('Arial',19))
    ent_soyad.place(x=105,y=60)
    
    lbl_yas = tk.Button(canvas_info,text = 'Yas     :', font = ('Algerian',15))
    lbl_yas.place(x=5,y=110)
    ent_yas = tk.Entry(canvas_info,font = ('Arial',19))
    ent_yas.place(x=105,y=110)
    
    lbl_adres = tk.Button(canvas_info,text = 'Adres:', font = ('Algerian',15))
    lbl_adres.place(x=5,y=160)
    ent_adres = tk.Entry(canvas_info,font = ('Arial',19))
    ent_adres.place(x=105,y=160)
lbl_info()
def veri_topla():
    
    new_window = tk.Toplevel()
    new_window.title('veri Toplama Formu')
    new_window.geometry('600x400+150+60')
    new_window.resizable(0,0)
    window.withdraw()
    ic_canvas1 = tk.Canvas(new_window,width=400,height=300)
    ic_canvas1.place(x=0,y=0)
    def Update():
            ret,frame = cap.read()
            s_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
            g_frame = cv2.cvtColor(s_frame,cv2.COLOR_BGR2RGB)
            face_locations = fr.face_locations(g_frame)
            for (top,right,bottom,left) in face_locations:
                top *=4
                right *=4
                bottom *=4
                left *=4
                cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
                
            img = Image.fromarray(frame)
            imgTk = ImageTk.PhotoImage(image = img)
            label_img = tk.Label(ic_canvas1,image=imgTk)
            label_img.image = imgTk
            label_img.place(x=5,y=5)
            
            label_img.after(20,Update)
    width = 390
    height = 290
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    Update()
    ic_canvas2 = tk.Canvas(new_window,width=200,height=300,bg='ivory')
    ic_canvas2.place(x=400,y=0)
    
    ic_canvas3 = tk.Canvas(new_window,width=600,height=100,bg='yellow')
    ic_canvas3.place(x=0,y=300)
    
    def resim_cek():
        img_id = 0
        if img_id >= 5:
            messagebox.showinfo('bildiri','yeterince resim cekildi !!!')
        while True:
            ret,frame = cap.read()
            g_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
            face_locations = fr.face_locations(g_frame)
            
            for (top,right,bottom,left) in face_locations:
                crop = g_frame[top:bottom,left:right]
                face_crop =cv2.resize(crop,(200,200))
                
                cv2.imwrite('data/'+ent_ad.get()+'.'+str(img_id)+'.jpg',face_crop)
                cv2.putText(face_crop, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                img_id +=1
            cv2.imshow('face',face_crop)
            if cv2.waitKey(1)==13 or int(img_id)==5:#13 is the ASCII character of Enter
                break
            
        
        resim = Image.open('data/'+str(ent_ad.get())+'.1'+'.jpg')
        photo = ImageTk.PhotoImage(resim)
        label_img = tk.Label(ic_canvas2,image=photo,width=200,height=200)
        label_img.image=photo
        label_img.place(x=5,y=5)
                        
        canvas_bilgi2 = tk.Canvas(ic_canvas2,width=200,height=150)
        canvas_bilgi2.place(x=5,y=160)
        a1 = tk.Label(canvas_bilgi2, text="Ad = ", font=("Algerian",15))
        a1.grid(column = 0, row = 0)
        b1 = tk.Label(canvas_bilgi2, text=ent_ad.get(), font=("Arial",15))
        b1.grid(column = 1, row = 0)

        c1 = tk.Label(canvas_bilgi2, text="Soyad = ", font=("Algerian",15))
        c1.grid(column = 0, row = 1)

        d1 = tk.Label(canvas_bilgi2, text = ent_soyad.get(), font=("Arial",15))
        d1.grid(column = 1, row = 1)

        e1 = tk.Label(canvas_bilgi2, text="Yas = ", font=("Algerian", 15))
        e1.grid(column = 0, row = 2)
        f1 = tk.Label(canvas_bilgi2, text= ent_yas.get(), font=("Arial",15))
        f1.grid(column = 1, row = 2)
        
        e1 = tk.Label(canvas_bilgi2, text="Adres = ", font=("Algerian", 15))
        e1.grid(column = 0, row = 3)
        f1 = tk.Label(canvas_bilgi2, text= ent_adres.get(), font=("Arial",15))
        f1.grid(column = 1, row = 3)
        
        id_info = tk.Label(canvas_bilgi2, text="ID = ", font=("Algerian", 15))
        id_info(column = 0, row = 4)
        id_info_val = tk.Label(canvas_bilgi2, text= img_id, font=("Arial",15))
        id_info_val.grid(column = 1, row = 4)

        # e1 = tk.Label(canvas_bilgi2, text="Cekilen resim =", font=("Algerian", 10))
        # e1.grid(column = 0, row = 3)
        # f1 = tk.Label(canvas_bilgi2, text=img_id , font=("Arial",10))
        # f1.grid(column = 1, row = 3)        
        ent_ad.delete(0,'end')
        ent_soyad.delete(0,'end')
        ent_yas.delete(0,'end')  
        ent_adres.delete(0,'end')       
        cv2.destroyAllWindows()       
        
    
    btn_r_cek = tk.Button(ic_canvas3,text = 'Resim Cek',font =('Algerian',20),bg='green',fg='black',command=resim_cek)
    btn_r_cek.place(x=5,y=30)
    
    def eixt():
        new_window.withdraw()
        cap.release()
        window.deiconify()
    
    btn_exit = tk.Button(ic_canvas3,text = 'Cikis Yap',font =('Algerian',20),bg='red',fg='white',command=eixt)
    btn_exit.place(x=180,y=30)
    
    new_window.mainloop()
    
    
btn_data = tk.Button(canvas_info,text = 'Veri Topla',font =('Algerian',20),bg='yellow',fg='black',command=veri_topla)
btn_data.place(x=120,y=250)

def train():
    pass
btn_data = tk.Button(canvas_btn,text = 'Verileri Egit',font =('Algerian',20),bg='orange',fg='black',width=20,command=train)
btn_data.place(x=10,y=25)

def video_captrue():
    #data = 'C:/Users/abdul/Documents/FaceRecogrition/Spider_Face/Image'
    data = 'data'
    myList = os.listdir(data)
    images = []
    img_names = []
    for img in myList:
        image = cv2.imread(f'{data}/{img}')
        images.append(image)
        img_names.append(os.path.splitext(img)[0].split('.')[0])
    
        
    def encod(images):
        encodList = []
        for img in images:
            
            img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            face_encod = fr.face_encodings(img_gray)[0]
            encodList.append(face_encod)
        return encodList
    
    know_encoding=encod(images)
    
        
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    
    cap = cv2.VideoCapture(0)
    
    while True:
        ret,frame = cap.read()
        
        s_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        g_frame = cv2.cvtColor(s_frame,cv2.COLOR_BGR2RGB)
        if process_this_frame:
            face_locations = fr.face_locations(g_frame)
            face_encodings = fr.face_encodings(g_frame,face_locations)
            
            face_names = []
            
            for face_encoding in face_encodings:
                matches = fr.compare_faces(know_encoding,face_encoding)
                name = 'Unknown'
                
                face_distence = fr.face_distance(know_encoding,face_encoding)
                best_match_index = np.argmin(face_distence)
                if matches[best_match_index]:
                    name = img_names[best_match_index]
                    
                face_names.append(name)
        process_this_frame = not process_this_frame
        
        for (top,right,bottom,left),name in zip(face_locations,face_names):
            top *=4
            right *=4
            bottom *=4
            left *=4
            
            cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
            cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,255,0),cv2.FILLED)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            frame_live() 
            break
        
    #cap.release()
    cv2.destroyAllWindows()
    
    
    
btn_data = tk.Button(canvas_btn,text = 'WebCam ile ',font =('Algerian',20),bg='silver',fg='black',width=20,command=video_captrue)
btn_data.place(x=10,y=100)

def image_capture():
    pass
btn_data = tk.Button(canvas_btn,text = 'Resim ile',font =('Algerian',20),bg='brown',fg='black',width=20,command=image_capture)
btn_data.place(x=400,y=25)

def cikis():
    window.destroy()
    cap.release()
    cv2.destroyAllWindows()
    import sys
    sys.exit()
btn_data = tk.Button(canvas_btn,text = 'Cikis',font =('Algerian',20),bg='red',fg='white',width=20,command=cikis)
btn_data.place(x=400,y=100)
window.mainloop()