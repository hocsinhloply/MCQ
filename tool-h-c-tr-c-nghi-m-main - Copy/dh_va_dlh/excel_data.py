import pandas as pd
import array
import random

test = pd.read_excel("C:\\Users\\DELL\\Desktop\\python\\dh_va_dlh\\question_ver2.xlsx", sheet_name="Nhóm 12")

STT = test['STT']
questions = test['Câu hỏi']
options = test[['A', 'B', 'C', 'D']]
answers = test['Đáp án đúng']
S = ['A', 'B', 'C', 'D']

question_number = list(STT)
question_number.remove(5)
print(question_number)