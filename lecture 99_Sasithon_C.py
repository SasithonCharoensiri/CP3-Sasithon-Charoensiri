from tkinter import *
import math

def leftClickButton(event):
    BMI = round(float(textboxWeight.get()) / math.pow(float(textboxHeight.get())/100,2))
    labelBMI.configure(text=BMI)
    if BMI < 18.55:
        labelResult.configure(text="อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม")
    elif BMI < 23:
        labelResult.configure(text="อยู่ในเกณฑ์ปกติ")
    elif BMI < 25:
        labelResult.configure(text="น้ำหนักเกิน")
    elif BMI < 30:
        labelResult.configure(text="โรคอ้วนระดับที่ 1")
    else :
        labelResult.configure(text="โรคอ้วนระดับที่ 2")

MainWindow = Tk()

labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)

textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)

textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="ผลลัพท์")
labelResult.grid(row=3,column=1)

labelBMI = Label(MainWindow, text="เกณฑ์")
labelBMI.grid(row=2,column=1)

MainWindow.mainloop()