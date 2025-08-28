import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.expression = ""
        
        self.bg_color = "#1D1D1D"
        self.entry_bg = "#1a1a1a"
        self.entry_fg = "#ffffff"
        self.btn_bg = "#3F3F3F"
        self.btn_fg = "#ffffff"
        self.op_bg = "#f9b049"    
        self.eq_bg = "#44cf66"    
        self.clear_bg = "#f0392f" 

        self.root.configure(bg=self.bg_color)

        self.entry = tk.Entry(
            root, font=("Arial", 22), bd=0, bg=self.entry_bg, fg=self.entry_fg,
            justify="right", insertbackground="white"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=5, ipady=15, sticky="nsew")

        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                if char == "C":
                    bg = self.clear_bg
                elif char == "=":
                    bg = self.eq_bg
                elif char in ["+", "-", "×", "÷"]:
                    bg = self.op_bg
                else:
                    bg = self.btn_bg

                btn = tk.Button(
                    root, text=char, font=("Arial", 18),
                    fg=self.btn_fg, bg=bg, activebackground="#555555",
                    relief="flat", command=lambda c=char: self.on_click(c)
                )
                btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(1, 5):
            self.root.grid_rowconfigure(i, weight=1)

    def on_click(self, char):
        if char == "C":  
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == "=":  
            try:
                expr = self.expression.replace("×", "*").replace("÷", "/")  # replace symbols
                result = str(eval(expr))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:  
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
