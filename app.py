import os
import shutil
import tkinter as tk
from tkinter import filedialog

folder1 = ""
folder2 = ""
folder3 = ""
folder4 = ""

def folder1_sellect():
    global folder1
    folder1 = filedialog.askdirectory(title="1. Select Folder")
    print("1. Selected:", folder1)
    label_text.set("1. Selected: " + folder1)

def folder2_sellect():
    global folder2
    folder2 = filedialog.askdirectory(title="2. Select Folder")
    print("2. Selected:", folder2)
    label_text.set("2. Selected: " + folder2)

def folder3_sellect():
    global folder3
    folder3 = filedialog.askdirectory(title="3. Select Folder")
    print("3. Selected:", folder3)
    label_text.set("3. Selected: " + folder3)

def folder4_sellect():
    global folder4
    folder4 = filedialog.askdirectory(title="4. Select Folder")
    print("4. Selected:", folder4)
    label_text.set("4. Selected: " + folder4)


def file_compare():
    if not folder1 or not folder2 or not folder3 or not folder4:
        print("Please select all folders!")
        label_text.set("Please select all folders!")
        return

    folders1 = os.listdir(folder1)
    folders3 = os.listdir(folder3)
    
    for file1 in folders1:
        for file3 in folders3:
            if file1 == file3:
                kaynak = os.path.join(folder1, file1)
                hedef = os.path.join(folder2, file1)
                shutil.move(kaynak, hedef)
                print(f"{file1} to {folder2}")
                label_text.set(f"{file1} to {folder2}")

    folders2 = os.listdir(folder2)

    for file3 in folders3:
        for file2 in folders2:
            if file3 == file2:
                kaynak = os.path.join(folder3, file3)
                hedef = os.path.join(folder4, file3)
                shutil.move(kaynak, hedef)
                print(f"{file3} to {folder4}")
                label_text.set(f"{file3} to {folder4}")

# GUI
root = tk.Tk()
root.geometry("300x250")
root.resizable(False, False)
root.title("Compare File")
root.iconbitmap("favicon.ico")

label_text = tk.StringVar()
label_text.set("Please select folders.")

label = tk.Label(root, textvariable=label_text)
label.pack(pady=10)

button1 = tk.Button(root, text="1st folder to compare", command=folder1_sellect)
button1.pack(pady=10)

button2 = tk.Button(root, text="Same files of the 1st folder", command=folder2_sellect)
button2.pack(pady=10)

button3 = tk.Button(root, text="2nd folder to compare", command=folder3_sellect)
button3.pack(pady=10)

button4 = tk.Button(root, text="Same files of the 2nd folder", command=folder4_sellect)
button4.pack(pady=10)

button_start = tk.Button(root, text="Start", command=file_compare)
button_start.pack(pady=20)

root.mainloop()
