import tkinter as tk

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            entry_var.set("Erro")
    else:
        entry_var.set(entry_var.get() + button_text)

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Variável que armazena a expressão
entry_var = tk.StringVar()

tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right').grid(row=0, column=0, columnspan=4)

# Layout dos botões
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        tk.Button(root, text=button, font=("Arial", 18), width=5, height=2,
                  command=lambda b=button: on_click(b)).grid(row=i+1, column=j)

# Executar a interface gráfica
root.mainloop()
