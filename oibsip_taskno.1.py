from tkinter import *
from tkinter import ttk

co0 = "#444466"  # black
co1 = "#feffff"  # white
co2 = "#8888aa"  # gray

window = Tk()
window.title('BMI Calculator')
window.geometry('500x250')
window.resizable(height=FALSE, width=FALSE)
window.configure(bg=co1)

top_frame = Frame(window, width=500, height=50, bg=co1, pady=0, padx=0)
top_frame.grid(row=0, column=0)

down_frame = Frame(window, width=500, height=200, bg=co1, pady=0, padx=0)
down_frame.grid(row=1, column=0)

app_name = Label(top_frame, text="BMI CALCULATOR", width=23, height=1, padx=0, anchor="center", font=("Ivy 16 bold"), bg=co1, fg=co0)
app_name.pack(expand=True)

app_line = Label(top_frame, text="", width=500, height=1, padx=0, anchor="center", font=("Arial 1"), bg=co2, fg=co0)
app_line.pack(fill=X)

def calculate():
    try:
        weight = float(e_weight.get())  # Weight in kg
        height = float(e_height.get()) / 100  # Height in meters (assuming input in cm)
        bmi = weight / (height ** 2)

        if bmi < 18.4:
            l_result_text['text'] = "Your BMI is: Underweight"
        elif 18.5 <= bmi < 24.9:
            l_result_text['text'] = "Your BMI is: Normal"
        elif 25 <= bmi < 29.9:
            l_result_text['text'] = "Your BMI is: Overweight"
        else:
            l_result_text['text'] = "Your BMI is: Obesity"

        l_result['text'] = "{:.2f}".format(bmi)

    except ValueError:
        l_result_text['text'] = "Please enter valid numbers"
        l_result['text'] = "----"

l_weight = Label(down_frame, text="Enter Your Weight (kg)", height=1, padx=0, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
l_weight.grid(row=0, column=0, columnspan=1, pady=10, padx=3)
e_weight = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="center", relief=SOLID)
e_weight.grid(row=0, column=1, columnspan=1, pady=10, padx=3)

l_height = Label(down_frame, text="Enter Your Height (cm)", height=1, padx=0, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
l_height.grid(row=1, column=0, columnspan=1, pady=10, padx=3)
e_height = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="center", relief=SOLID)
e_height.grid(row=1, column=1, columnspan=1, pady=10, padx=3)

l_result = Label(down_frame, width=12, text="----", height=1, padx=6, pady=12, anchor="center", font=('Ivy 24 bold'), bg=co2, fg=co1)
l_result.grid(row=0, column=2, rowspan=2, pady=10, padx=10)

l_result_text = Label(down_frame, width=55, text="", height=1, padx=6, pady=12, anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_result_text.grid(row=2, column=0, columnspan=3, pady=10, padx=3)

b_calculate = Button(down_frame, text="Calculate", width=45, height=1, bg=co2, fg=co1, font=("Ivy 10 bold"), anchor="center", command=calculate)
b_calculate.grid(row=3, column=0, columnspan=3, pady=20, padx=5)

window.mainloop()


