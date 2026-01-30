import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
display = tk.Entry(root,font=("Arial", 16),borderwidth=5,justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
buttons = [('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),('0',4,0), ('.',4,1), ('+',4,2),('C',5,0), ('=',5,1)]
for text, r, c in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 14))
    if text == '+':
        btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=5, pady=5)
    elif text == '=':
        btn.grid(row=r, column=c, columnspan=3, sticky="nsew", padx=5, pady=5)
    else:
        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
        
root.mainloop()
