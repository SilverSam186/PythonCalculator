import tkinter as tk
import math

def cos(x):
    angle_rad = math.radians(float(x))
    return math.cos(angle_rad)

def sin(x):
    angle_rad = math.radians(float(x))
    return math.sin(angle_rad)

def tan(x):
    angle_rad = math.radians(float(x))
    return math.tan(angle_rad)

# =========================
# Colors & styling
bg_color = "#2b2b2b"
button_color = "#444444"
button_hover = "#555555"
text_color = "#ffffff"
display_color = "#1e1e1e"
text_display_color = "#1e1e1e"

# =========================
# Window setup
window = tk.Tk()
window.title("Ultimate Scientific Calculator")
window.geometry("700x550")
window.configure(bg=bg_color)
window.resizable(False, False)

# =========================
# Grid configuration
for i in range(8):
    window.rowconfigure(i, weight=1)
for i in range(6):
    window.columnconfigure(i, weight=1)

# =========================
# Display using StringVar
display_var = tk.StringVar()
display = tk.Entry(window, font=("Arial", 24), justify="right",
                   textvariable=display_var, bg=display_color,
                   fg=text_display_color, borderwidth=5, state='readonly')
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
display.focus_set()

# =========================
# History panel
history = tk.Text(window, height=10, width=30, font=("Arial", 12),
                  state='disabled', borderwidth=2, bg=display_color, fg=text_color)
history.grid(row=0, column=5, rowspan=8, padx=5, pady=5, sticky="nsew")

# =========================
# Helper math functions
def safe_sin(x):
    return math.sin(math.radians(float(x)))

def safe_cos(x):
    return math.cos(math.radians(float(x)))

def safe_tan(x):
    return math.tan(math.radians(float(x)))

def safe_sqrt(x):
    print("Calculating sqrt of:", x)
    return math.sqrt(float(x))

def safe_log(x):
    return math.log(float(x))

def safe_abs(x):
    return abs(float(x))

def safe_factorial(x):
    return math.factorial(int(float(x)))

# =========================
# Memory storage
memory = 0

def set_display(text):
    display.configure(state='normal')
    display_var.set(text)
    display.configure(state='readonly')

def click(value):
    current = display_var.get()

    functions = ["sin", "cos", "tan", "log", "abs"]

    if value in functions:
        set_display(current + value + "(")

    elif value == "√":
        set_display(current + "sqrt(")

    else:
        set_display(current + str(value))

def clear():
    set_display("")

def backspace():
    current = display_var.get()
    set_display(current[:-1])

def calculate():
    try:
        expression = display_var.get()
        expression_eval = expression.replace("^", "**").replace("√", "sqrt").replace("π", "pi")

        print("Evaluating:", expression_eval)

        result = eval(expression_eval, {"__builtins__": None}, {
            "sin": safe_sin,
            "cos": safe_cos,
            "tan": safe_tan,
            "sqrt": safe_sqrt,
            "log": safe_log,
            "abs": safe_abs,
            "factorial": safe_factorial,
            "pi": math.pi,
            "exp": math.exp
        })

        set_display(result)

        history.config(state='normal')
        history.insert(tk.END, f"{expression} = {result}\n")
        history.see(tk.END)
        history.config(state='disabled')

    except:
        set_display("Error")

def clear_history():
    history.config(state='normal')
    history.delete('1.0', tk.END)
    history.config(state='disabled')

# =========================
# Memory functions
def memory_store():
    global memory
    try:
        memory = float(display_var.get())
    except:
        pass

def memory_recall():
    set_display(str(memory))

def memory_add():
    global memory
    try:
        memory += float(display_var.get())
    except:
        pass

def memory_subtract():
    global memory
    try:
        memory -= float(display_var.get())
    except:
        pass

# =========================
# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sin',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('cos',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('tan',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), ('√',4,4),
    ('C',5,0), ('⌫',5,1), ('π',5,2), ('log',5,3), ('^',5,4),
    ('M+',6,0), ('M-',6,1), ('MR',6,2), ('MS',6,3), ('abs',6,4),
    ('(', 7,[0, 2]), (')', 7,[2, 4]), ('', 7,4)
]

for (text,row,col) in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    elif text == "⌫":
        cmd = backspace
    elif text == "M+":
        cmd = memory_add
    elif text == "M-":
        cmd = memory_subtract
    elif text == "MR":
        cmd = memory_recall
    elif text == "MS":
        cmd = memory_store
    else:
        cmd = lambda t=text: click(t)

    if isinstance(col, list):
        columnstart = col[0]
        columnspan = col[1] - col[0]
    else:
        columnstart = col
        columnspan = 1

    tk.Button(window, text=text, font=("Arial",16), bg=button_color, fg=text_color,
              activebackground=button_hover, relief="raised", bd=3, command=cmd)\
        .grid(row=row, column=columnstart, columnspan=columnspan, sticky="nsew", padx=3, pady=3)

# =========================
# History clear button
tk.Button(window, text="Clear History", font=("Arial",12),
          bg=button_color, fg=text_color, activebackground=button_hover,
          command=clear_history)\
    .grid(row=7, column=5, padx=5, pady=5, sticky="nsew")

# =========================
# Keyboard input
def key_input(event):
    key = event.char
    
    if key in "0123456789+-*/.^":
        click(key)
        return "break"
    elif event.keysym == "Return":
        calculate()
        return "break"
    elif event.keysym == "BackSpace":
        backspace()
        return "break"
    elif key.lower() == "c":
        clear()
        return "break"

display.bind("<Key>", key_input)

window.mainloop()