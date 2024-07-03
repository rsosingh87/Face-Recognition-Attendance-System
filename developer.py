from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1255,height=35)
        
        img_top=Image.open(r"E:\Face Recognitio System\collect images\united.jpeg")
        img_top=img_top.resize((1255,300),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=60,width=1255,height=300)
        
        # Frame 
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=500,y=0,width=300,height=485)
        
        
        img_top1=Image.open(r"E:\Face Recognitio System\collect images\collect images\Rishi.JPG")
        img_top1=img_top.resize((200,200),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top)

        f_lbl=Label(main_frame,image=self.photoimg_top)
        f_lbl.place(x=200,y=60,width=200,height=200)
        
        
        
        
        
        
        
                                                                                                                                                                  
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
 