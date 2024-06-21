import tkinter as tk
from tkinter import StringVar
import pandas as pd
import random
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('1000x700')

# sheetName = ["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4", "Nhóm 5", "Nhóm 6", 
#               "Nhóm 7", "Nhóm 8", "Nhóm 9", "Nhóm 10", "Nhóm 11", "Nhóm 12", 
#               "Nhóm 13", "Nhóm 14", "Nhóm 15", "Nhóm 16", "Nhóm 17", "FULL", "1-10", "11-17"]
print("Điền tên nhóm")
sheetName = input() # đổi tên sheet ở đây
#test = pd.read_excel("C:\\Users\\DELL\\Desktop\\python\\dh_va_dlh\\question2.xlsx", sheet_name=sheetName)
test = pd.read_excel("question2.xlsx", sheet_name=sheetName)

STT = test['STT']
questions = test['Câu hỏi']
options = test[['A', 'B', 'C', 'D']]
answers = test['Đáp án đúng']
S = ['A', 'B', 'C', 'D']
image_question1 = [25, 26, 27, 28, 29, 30]
image_question2 = [225, 226, 227, 228, 229, 230, 269]

#my_image = ImageTk.PhotoImage(Image.open("C:/Users/DELL/Desktop/python/dh_va_dlh/image/none.png"))
my_image = ImageTk.PhotoImage(Image.open("image/none.png"))

frame = tk.Frame(root, padx=10, pady=10)
question_label = tk.Label(frame,height=6, width=80,bg='light blue',fg="black", 
                          font=('Verdana', 15),wraplength=900)
picture_label = tk.Label(frame, image=my_image)
check_label = tk.Label(frame, font=('Verdana', 10))

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 12), wraplength=900, 
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 12), wraplength=900, 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 12), wraplength=900, 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 12), wraplength=900, 
                         command = lambda : checkAnswer(option4))

button_A = tk.Button(frame, text = 'A', bg='#fff', font=('Verdana', 12))
button_B = tk.Button(frame, text = 'B', bg='#fff', font=('Verdana', 12))
button_C = tk.Button(frame, text = 'C', bg='#fff', font=('Verdana', 12))
button_D = tk.Button(frame, text = 'D', bg='#fff', font=('Verdana', 12))

button_next = tk.Button(frame, text='Câu tiếp theo',bg='Orange', font=('Verdana', 15), 
                        command = lambda : displayNextQuestion())

button_quit = tk.Button(frame, text='Kết thúc',bg='Orange', font=('Verdana', 15), 
                        command = root.destroy)

frame.pack(fill="both", expand="true")
#picture_label.grid(row=0, column=0)
question_label.grid(row=1, column=0)
check_label.place(x=0,y=0)

option1.grid(sticky= 'W', row=2, column=0)
option2.grid(sticky= 'W', row=3, column=0)
option3.grid(sticky= 'W', row=4, column=0)
option4.grid(sticky= 'W', row=5, column=0)

button_A.grid(sticky= 'W', row=2, column=0)
button_B.grid(sticky= 'W', row=3, column=0)
button_C.grid(sticky= 'W', row=4, column=0)
button_D.grid(sticky= 'W', row=5, column=0)

button_next.grid(row=7, column=0)
button_quit.grid(row=9, column=0)

correct = 0
wrong = 0
number_of_question = list(STT)
question_number = random.choice(number_of_question)
user_answer = ''
check_label['text'] = "Đúng: " + str(correct) + "/" + str(len(STT)) + "\nSai: " + str(wrong) + "/" + str(len(STT))

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

# create a function to check the selected answer
def checkAnswer(radio):
    global correct, wrong, question_number, user_answer, check_label
    
    user_answer = radio['text']
    if user_answer != answers[question_number - 1]:
        wrong+=1
        if option1['text'] == user_answer :
            button_A['bg'] = 'red'
        if option2['text'] == user_answer :
            button_B['bg'] = 'red'
        if option3['text'] == user_answer :
            button_C['bg'] = 'red'
        if option4['text'] == user_answer :
            button_D['bg'] = 'red'
        if option1['text'] == answers[question_number - 1] :
            button_A['bg'] = 'green'
        if option2['text'] == answers[question_number - 1] :
            button_B['bg'] = 'green'
        if option3['text'] == answers[question_number - 1] :
            button_C['bg'] = 'green'
        if option4['text'] == answers[question_number - 1] :
            button_D['bg'] = 'green'
    
    if user_answer == answers[question_number - 1]:
        correct +=1
        if option1['text'] == user_answer :
            button_A['bg'] = 'green'
        if option2['text'] == user_answer :
            button_B['bg'] = 'green'
        if option3['text'] == user_answer :
            button_C['bg'] = 'green'
        if option4['text'] == user_answer :
            button_D['bg'] = 'green'
    
    check_label['text'] = "Đúng: " + str(correct) + "/" + str(len(STT)) + "\nSai: " + str(wrong) + "/" + str(len(STT))
    disableButtons('disable')

# create a function to display the next question
def displayNextQuestion():
    global correct, wrong, question_number, S, my_image, number_of_question, check_label
    
    question_number = random.choice(number_of_question)
    number_of_question.remove(question_number)

    if button_next['text'] == 'Bắt đầu lại':
        correct = 0
        wrong = 0
        check_label['text'] = "Đúng: " + str(correct) + "/" + str(len(STT)) + "\nSai: " + str(wrong) + "/" + str(len(STT))
        question_label['text'] = "Câu " + str(question_number) + ": " + questions[question_number - 1]
        question_label['bg'] = 'light blue'
        button_next['text'] = 'Next'
        picture_label['image'] = my_image

    else:
        if question_number in image_question1 and sheetName == "Nhóm 17":
            my_image = ImageTk.PhotoImage(Image.open("image/" + str(question_number) + ".png"))
            picture_label.grid(row=0, column=0)
            #picture_label.place(x = 500, y = 500)
        elif question_number in image_question2 and sheetName == "FULL":
            my_image = ImageTk.PhotoImage(Image.open("image/" + str(question_number) + ".png"))
            picture_label.grid(row=0, column=0)
        else:
            picture_label.grid_forget()

        question_label['text'] = "Câu " + str(question_number) + ": " + questions[question_number - 1]
        picture_label['image'] = my_image

        if len(number_of_question) == 0:
            number_of_question = list(STT)
            question_label['text'] = "Câu " + str(question_number) + ": " + questions[question_number - 1]
            button_next['text'] = 'Bắt đầu lại'

    disableButtons('normal')
    S = random.sample(S, 4)
    option1['text'] = options[S[0]][question_number - 1]
    option2['text'] = options[S[1]][question_number - 1]
    option3['text'] = options[S[2]][question_number - 1]
    option4['text'] = options[S[3]][question_number - 1]
    button_A['bg'] = 'white'
    button_B['bg'] = 'white'
    button_C['bg'] = 'white'
    button_D['bg'] = 'white'
    v1.set(option1['text'])
    v2.set(option2['text'])
    v3.set(option3['text'])
    v4.set(option4['text'])

displayNextQuestion()

root.mainloop()