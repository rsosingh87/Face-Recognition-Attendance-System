from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img=Image.open(r"E:\Face Recognitio System\collect images\stanford.jpeg")
        img=img.resize((420,110),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=420,height=110)
        
        #Second Image 
        img1=Image.open(r"E:\Face Recognitio System\collect images\Face.jpg")
        img1=img1.resize((420,110),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=420,y=0,width=420,height=110)
        
        #Third Image 
        img2=Image.open(r"E:\Face Recognitio System\collect images\united.jpeg")
        img2=img2.resize((420,110),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=840,y=0,width=430,height=110)
        
        #bg imag3
        img3=Image.open(r"E:\Face Recognitio System\collect images\bg.jpg")
        img3=img3.resize((1420,530),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=110,width=1420,height=530)
        
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1290,height=35)
        
        
        #student button
        img4=Image.open(r"E:\Face Recognitio System\collect images\first.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=70,width=170,height=150)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=200,width=170,height=30)
        
        
        #Detect face button
        img5=Image.open(r"E:\Face Recognitio System\collect images\face detection.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=170,height=150)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=200,width=170,height=30)
        
        
        
        #Attendence face button
        img6=Image.open(r"E:\Face Recognitio System\collect images\attendance.png")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=650,y=70,width=170,height=150)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=200,width=170,height=30)
        
        
        #Help face button
        img7=Image.open(r"E:\Face Recognitio System\collect images\help desk.png")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=900,y=70,width=170,height=150)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=200,width=170,height=30)
        
        
        
        #Train face button
        img8=Image.open(r"E:\Face Recognitio System\collect images\train.png")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=280,width=170,height=150)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=410,width=170,height=30)
        
        #photos face button
        img9=Image.open(r"E:\Face Recognitio System\collect images\photos.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=280,width=170,height=150)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=410,width=170,height=30)
        
        #Developer face button
        img10=Image.open(r"E:\Face Recognitio System\collect images\developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=650,y=280,width=170,height=150)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=410,width=170,height=30)
        
        #Exit face button
        img11=Image.open(r"E:\Face Recognitio System\collect images\exit.png")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=900,y=280,width=170,height=150)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=410,width=170,height=30)
        
    def open_img(self):
        os.startfile("data")
            
              
            
        
        #Function Buttons 
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)  
          
    def attendace_data(self):
        self.new_window=Toplevel(self.root)
        #self.app=Attendance(self.new_window)      
        

        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
