import tkinter as tk
# from tkinter import *
# from PIL import Image, ImageTk
# import string

group_button = ["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4", "Nhóm 5", "Nhóm 6", 
                "Nhóm 7", "Nhóm 8", "Nhóm 9", "Nhóm 10", "Nhóm 11", "Nhóm 12", 
                "Nhóm 13", "Nhóm 14", "Nhóm 15", "Nhóm 16", "Nhóm 17", "FULL"]

root = tk.Tk()
root.geometry('1000x700')


frame = tk.Frame(root)
frame.pack(fill="both")
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)

question_label = tk.Label(frame,height=6, width=80,bg='light blue',fg="black", 
                          font=('Verdana', 15),wraplength=900)
question_label.grid(row=1, column=0)
button = list()
for i in range(4):
    button.append(tk.Button(frame1, text=group_button[i]))#, image=karirano, command=partial(klik, i)))
    button[-1].grid(row=2,column=i)
root.mainloop()
