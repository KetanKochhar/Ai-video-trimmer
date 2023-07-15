from customtkinter import *
import customtkinter as c
import os 
import shutil as s 
import docx
import trim

# set the theme of screen 
c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")


# functions for oprating the GUI
def openfolder():
    folder = filedialog.askopenfilenames()
    for x in range(len(folder)):
        if folder[x][-1] == "4":
            print("true")
            if folder[x][-1] == "p":
                print("true")
                if folder[x][-1] == "m":
                    write(folder[x])
    def write(txt):
        f = open("temp.txt" , "a")
        f.write(txt)
        f.close()
# def openfolder():
#     openfolder = filedialog.askopenfilenames()
#     print(openfolder)
#     for x in range(len(openfolder)):
#         if openfolder[x][-1] == "4":
#             if openfolder[x][-1] == "p":
#                 if openfolder[x][-1] == "m":
#                     f = open("temp.txt" , "w")
#                     f.write(openfolder)
#                     f.writable(0)
#                     f.close()
#     # print(len(os.listdir(openfolder)))
#     # for x in range(len(os.listdir(openfolder))):
#     #     tit = os.listdir(openfolder)[x]
#     #     print(tit)
#     #     msg = CTkLabel(select , text= tit , font=("Arial" , 22 , "bold"))
#     #     msg.pack(pady=20)
#     option.forget()
#     option1.forget()
#     option2.forget()
def menu():
    renaming.forget()
    option.pack(fill=BOTH)
    option1.pack(fill=BOTH)
    option2.pack(fill=BOTH)
def renameFile():
    rename.forget()
    msg2 = CTkLabel(renaming , text="Files have been renamed acoording to the document that were bold in word file" , font=("Arial" , 20 , "bold"))
    msg2.pack(pady=20)
    f = open("temp.txt" , "r")
    data = f.readlines()
    print(data[0])
    doc = docx.Document(data[0])
    auto = []
    title = []
    for x in doc.paragraphs: #para
        for a in x.runs:#sente
            if a.bold:
                data = a.text
                title.append(data)
            #    print(a.text)
    # print(title)
    renameVID = []
    old = ""
    new = ""
    for x in os.listdir("output"):
        auto.append(x)
    #    print(x)
    for name in range(len(title)):
        old = "output//"+auto[name]
        new = "output//"+title[name]+".mp4"
        name=(old , new)
        renameVID.append(name)
        # rename.append(old)
        # rename.append(new)

    for x in renameVID :
        os.rename(x[0] , x[1])
    msg = CTkLabel(renaming , text="Video editing is been finished now go to main menu for uploading process")
    msg.pack(pady=30)
    ret = CTkLabel(renaming , text="Click the button to rfeturn to main menu" , font=("Arial" , 22 , "bold"))
    ret.pack(side="left" , pady=20)
    retb = CTkButton(renaming , text="click to return" , font=("Arial" , 22 , "bold") , command=menu)
    retb.pack(side="left" , padx=20)

def choosedocx ():
    msg = CTkLabel(rename , text="Choose the docx file to rename the videoes" , font=("Arial" , 22 , "bold"))
    msg.pack()
    msg1 = CTkLabel(rename , text="click to choose file " , font=("Arial" , 20 , "bold"))
    msg1.pack(pady=20 , side="left")
    btn1 = CTkButton(rename , text="Choose docx file" , command=OpenDocxFile)
    btn1.pack(padx=50 , side="left" , pady=20)
    fod.forget()

def rmdir():
    if os.path.exists("output"):
        s.rmtree("output")
def create_folder():
    if os.path.exists("output"):
        rmdir()
    os.system("mkdir output")
    rmf = CTkLabel(fod , text="New output folder is created sucessfully" , font=("Arial" , 20 , "bold"))
    rmf.pack(pady=30)
    ormf = CTkLabel(fod , text="Old one is been deleted" , font=("Arial" , 20 , "bold"))
    ormf.pack(pady=10)
    UpTxt = CTkLabel(fod , text="click the button to start the process " , font=("Arial" , 20  , "bold"))
    UpTxt.pack(pady=30 , side="left")
    def StartProcess():
        rmf.forget()
        ormf.forget()
        trim.trim()
        choosedocx()
    upbtn = CTkButton(fod , text="Start Triming" , command=StartProcess)
    upbtn.pack(padx=50)
    option.forget()
    option1.forget()
    option2.forget()
    # fod.forget()


def fail():
    messg = CTkFrame(title)
    messg.pack(fill=BOTH)
    msg2 = CTkLabel(messg , text="This is not required file" , font=("Arial" , 20  , "bold"))
    msg2.pack()
    option.forget()
    option2.forget()

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path[-1] == "4" or "v":
        if file_path [-2] == "p" or "k":
            if file_path[-3]== "m":
                f = open("temp.txt" , "w")
                f.write(file_path)
                f.close()
                create_folder()
                # sucess()
    else:
        fail()

def OpenDocxFile():
    FP = filedialog.askopenfilename()
    if FP[-1] == "x":
        if FP[-2] == "c":
            if FP[-3] == "o":
                if FP[-4] == "d":
                    f2 = open("temp.txt" , "w")
                    f2.write(FP)
                    f2.close()
                    renameFile()
    else :
        fail()
# seeting up the screen 
root = c.CTk() #screen created
root.title("BOT FOR SOCIAL MEDIA") #title of the screen 
root.geometry("1000x500") #resolution of the geometry

title = CTkFrame(root) # created the part inside the screen 
title.pack(fill=BOTH) # screen is expandable 

name = CTkLabel(title , text="Bot that trims the video and upload on youtube" , font=("Arial", 30, "bold"))
name.pack()

option = CTkFrame(root)
option.pack(fill=BOTH)

Txt = CTkLabel(option , text="Download the required files " , font=("Arial", 24, "bold"))
Txt.pack(side="left" , padx=30 , pady=30)

button = c.CTkButton(option, text="Click Me")
button.pack(side="right" , padx=30)

option1 = CTkFrame(root)
option1.pack(fill=BOTH)

Txt1 = CTkLabel(option1 , text="Choose the file that has to be trimmed " , font=("Arial", 24, "bold"))
Txt1.pack(side="left" , padx=30 , pady=30)

button1 = c.CTkButton(option1, text="Open File" , command=open_file)
button1.pack(side="right" , padx=30)

option2 = CTkFrame(root)
option2.pack(fill=BOTH)

Txt2 = CTkLabel(option2 , text="Upload video on youtube " , font=("Arial", 24, "bold"))
Txt2.pack(side="left" , pady=30 , padx=50)

button2 = c.CTkButton(option2, text="Open Folder" , command=openfolder)
button2.pack(side="right" , padx=30 )

fod = CTkFrame(root)
fod.pack(fill=BOTH)

rename = CTkFrame(root)    
rename.pack(fill=BOTH)

renaming = CTkFrame(root)
renaming.pack(fill=BOTH)

select = CTkFrame(root)
select.pack(fill=BOTH)
sel = CTkLabel(option2 , text="hello ")

root.mainloop()
