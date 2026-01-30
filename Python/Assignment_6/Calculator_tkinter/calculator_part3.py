import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

first_number = None
operator = None

def button_click(value):
    current = display_var.get()
    if value == '.' and '.' in current:
        return
    display_var.set(current + value)

def button_clear():
    global first_number, operator
    display_var.set("")
    first_number = None
    operator = None

def button_operator(op):
    global first_number, operator
    try:
        first_number = float(display_var.get())
        operator = op
        display_var.set("")
    except:
        display_var.set("Error")

def button_equals():
    global first_number, operator
    try:
        second_number = float(display_var.get())
        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        elif operator == '/':
            if second_number == 0:
                display_var.set("Error")
                return
            result = first_number / second_number
        else:
            return
        if result == int(result):
            display_var.set(str(int(result)))
        else:
            display_var.set(str(result))
    except:
        display_var.set("Error")
    first_number = None
    operator = None
    
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
display_var = tk.StringVar()
display = tk.Entry(root,font=("Arial", 16),borderwidth=5,justify="right",textvariable=display_var)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
buttons = [('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),('0',4,0), ('.',4,1), ('+',4,2),('C',5,0), ('=',5,1)]

for text, r, c in buttons:
    if text == 'C':
        cmd = button_clear
    elif text == '=':
        cmd = button_equals
    elif text in ['+','-','*','/']:
        cmd = lambda t=text: button_operator(t)
    else:
        cmd = lambda t=text: button_click(t)
    btn = tk.Button(root, text=text, font=("Arial", 14), command=cmd)
    if text == '+':
        btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=5, pady=5)
    elif text == '=':
        btn.grid(row=r, column=c, columnspan=3, sticky="nsew", padx=5, pady=5)
    else:
        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

root.mainloop()
