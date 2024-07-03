from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
#import cv2.face


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1255,height=35)
        
        img_top=Image.open(r"E:\Face Recognitio System\collect images\united.jpeg")
        img_top=img_top.resize((1255,300),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1255,height=280)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=310,width=1255,height=50)
        
        
        img_bottom=Image.open(r"E:\Face Recognitio System\collect images\united.jpeg")
        img_bottom=img_bottom.resize((1255,300),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=350,width=1255,height=280)
        
        
    def train_classifier(self):
        data_dir=("E:\Face Recognitio System\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #Greay scale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train Classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        #face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")

        




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()