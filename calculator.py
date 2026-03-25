import tkinter as tk
import math

# =========================
# Colors for Dark Mode
bg_color = "#2b2b2b"
button_color = "#444444"
button_hover = "#555555"
text_color = "#CFBEBE"
display_color = "#1e1e1e"

# =========================
# Window
window = tk.Tk()
window.title("Sam's Scientific Calculator")
window.geometry("650x500")
window.resizable(False, False)
window.configure(bg=bg_color)

# =========================
# Grid configuration
for i in range(7):
    window.rowconfigure(i, weight=1)
for i in range(6):
    window.columnconfigure(i, weight=1)

# =========================
# Display
display = tk.Entry(window, font=("Arial", 22), justify="right", borderwidth=5,
                   bg=display_color, fg=text_color, insertbackground=text_color, state='readonly')
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# =========================
# History Panel
history = tk.Text(window, height=10, width=25, font=("Arial", 12),
                  state='disabled', borderwidth=2, bg=display_color, fg=text_color)
history.grid(row=0, column=5, rowspan=7, padx=5, pady=5, sticky="nsew")

# =========================
# Safe math environment
safe_math = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log,
    "pi": math.pi
}

# =========================
# Functions
def set_display(text):
    display.configure(state='normal')
    display.delete(0, tk.END)
    display.insert(0, text)
    display.configure(state='readonly')

def click(value):
    display.configure(state='normal')
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))
    display.configure(state='readonly')

def clear():
    set_display("")

def backspace():
    display.configure(state='normal')
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])
    display.configure(state='readonly')

def calculate():
    try:
        display.configure(state='normal')
        expression = display.get()
        expression_eval = expression.replace("^", "**")
        expression_eval = expression_eval.replace("√", "sqrt")
        expression_eval = expression_eval.replace("π", "pi")
        result = eval(expression_eval, {"__builtins__": None}, safe_math)
        set_display(result)

        # Update history
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
# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0), ('⌫',5,1)  # Clear and Backspace buttons
]

for (text,row,col) in buttons:
    if text == "=":
        tk.Button(window, text=text, font=("Arial",16),
                  bg=button_color, fg=text_color, activebackground=button_hover,
                  command=calculate)\
            .grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
    elif text == "C":
        tk.Button(window, text=text, font=("Arial",16),
                  bg=button_color, fg=text_color, activebackground=button_hover,
                  command=clear)\
            .grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
    elif text == "⌫":
        tk.Button(window, text=text, font=("Arial",16),
                  bg=button_color, fg=text_color, activebackground=button_hover,
                  command=backspace)\
            .grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
    else:
        tk.Button(window, text=text, font=("Arial",16),
                  bg=button_color, fg=text_color, activebackground=button_hover,
                  command=lambda t=text: click(t))\
            .grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

# =========================
# Scientific Buttons
scientific_buttons = [
    ('sin',1,4), ('cos',2,4), ('tan',3,4), ('√',4,4),
    ('π',5,4), ('log',6,4), ('^',6,3)
]

for (text,row,col) in scientific_buttons:
    tk.Button(window, text=text, font=("Arial",14),
              bg=button_color, fg=text_color, activebackground=button_hover,
              command=lambda t=text: click(t))\
        .grid(row=row,column=col,sticky="nsew",padx=3,pady=3)

# =========================
# History Clear Button
tk.Button(window, text="Clear History", font=("Arial",12),
          bg=button_color, fg=text_color, activebackground=button_hover,
          command=clear_history)\
    .grid(row=7, column=5, padx=5, pady=5, sticky="nsew")

# =========================
# Keyboard Support (bind only to display)
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

# =========================
window.mainloop()