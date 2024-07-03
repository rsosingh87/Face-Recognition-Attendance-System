from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
from datetime import datetime
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1255, height=35)

        # First image
        img_top = Image.open(r"E:\Face Recognitio System\collect images\united.jpeg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=650, height=700)

        # Second image
        img_bottom = Image.open(r"E:\Face Recognitio System\collect images\united.jpeg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=40, width=950, height=700)

        # Button
        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=200, y=200, width=200, height=40)

    def mark_attendance(self, i, r, n, d):
        try:
            with open("Rishi.csv", "a+") as f:
            # Check if any of the identifiers already exist in the file
                f.seek(0)  # Move the file pointer to the beginning to read existing data
                existing_data = f.readlines()
                for line in existing_data:
                    entry = line.strip().split(",")
                    if len(entry) >= 4 and (i == entry[0] or r == entry[1] or n == entry[2] or d == entry[3]):
                        return  # If any identifier already exists, don't write duplicate entry

            # Write the new entry
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{i},{r},{n},{d},{dtString},{d1},present\n")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:",e)

    #-------------Face Recogniton----------------#
    
    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:   
            ret, img = video_cap.read() 
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = faceCascade.detectMultiScale(gray_img, 1.1, 4)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="RjanviS@12345678", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                result = my_cursor.fetchone()
                n = result[0] if result else "Unknown"

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                result = my_cursor.fetchone()
                r = result[0] if result else "Unknown"

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                result = my_cursor.fetchone()
                d = result[0] if result else "Unknown"

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                result = my_cursor.fetchone()
                i = result[0] if result else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y-70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d) 
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
