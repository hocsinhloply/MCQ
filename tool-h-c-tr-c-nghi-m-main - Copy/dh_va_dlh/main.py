import tkinter as tk
from tkinter import StringVar
import pandas as pd
import random
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('1000x700')

test = pd.read_excel("C:\\Users\\DELL\\Desktop\\python\\dh_va_dlh\\question.xlsx")

STT = test['STT']
questions = test['Câu hỏi']
options = test[['A', 'B', 'C', 'D']]
answers = test['Đáp án đúng']
S = ['A', 'B', 'C', 'D']
image_question = [225, 226, 227, 228, 229, 230, 269]

my_image = ImageTk.PhotoImage(Image.open("C:/Users/DELL/Desktop/python/dh_va_dlh/image/none.png"))

frame = tk.Frame(root, padx=10, pady=10)#,bg='#fff')
question_label = tk.Label(frame,height=6, width=80,bg='light blue',fg="black", 
                          font=('Verdana', 15),wraplength=900)
picture_label = tk.Label(frame, image=my_image)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 10), wraplength=900, 
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 10), wraplength=900, 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 10), wraplength=900, 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 10), wraplength=900, 
                         command = lambda : checkAnswer(option4))

button_A = tk.Button(frame, text = 'A', bg='#fff', font=('Verdana', 10))
button_B = tk.Button(frame, text = 'B', bg='#fff', font=('Verdana', 10))
button_C = tk.Button(frame, text = 'C', bg='#fff', font=('Verdana', 10))
button_D = tk.Button(frame, text = 'D', bg='#fff', font=('Verdana', 10))

button_next = tk.Button(frame, text='Câu tiếp theo',bg='Orange', font=('Verdana', 15), 
                        command = lambda : displayNextQuestion())

button_quit = tk.Button(frame, text='Kết thúc',bg='Orange', font=('Verdana', 15), 
                        command = root.destroy)

frame.pack(fill="both", expand="true")
picture_label.grid(row=0, column=0)
question_label.grid(row=1, column=0)

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
answered_question = 0
question_number = random.choice(STT)
user_answer = ''

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

# create a function to check the selected answer
def checkAnswer(radio):
    global correct, question_number, user_answer, answered_question
    
    answered_question += 1
    user_answer = radio['text']
    if user_answer != answers[question_number - 1]:
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
    
    disableButtons('disable')

# create a function to display the next question
def displayNextQuestion():
    global correct, question_number, answered_question, S, my_image
    my_image = ImageTk.PhotoImage(Image.open("C:/Users/DELL/Desktop/python/dh_va_dlh/image/none.png"))
    question_number = random.choice(STT)
    print(question_number)
    print(type(question_number))
    if button_next['text'] == 'Bắt đầu lại':
        correct = 0
        answered_question = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'
        picture_label['image'] = my_image

    else:
        if question_number in image_question:
            my_image = ImageTk.PhotoImage(Image.open("C:/Users/DELL/Desktop/python/dh_va_dlh/image/" + str(question_number) + ".png"))

        question_label['text'] = "Câu " + str(question_number) + ": " + questions[question_number - 1]
        picture_label['image'] = my_image
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