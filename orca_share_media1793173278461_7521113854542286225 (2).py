import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)
        self.configure(bg="#222831")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Arial", 28),
            justify="right",
            bd=0,
            bg="#393E46",
            fg="white",
            readonlybackground="#393E46",
            state="readonly",
        )
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=12, sticky="nsew")

        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, text in enumerate(row):
                span = 2 if text == "0" else 1
                if text == "0":
                    col = 0
                elif text == ".":
                    col = 2
                elif text == "=":
                    col = 3
                else:
                    col = c
                self.make_button(text, r, col, span)

        for i in range(4):
            self.columnconfigure(i, weight=1)

        self.bind("<Key>", self.on_key)
        self.bind("<Return>", lambda e: self.press("="))
        self.bind("<BackSpace>", lambda e: self.press("⌫"))
        self.bind("<Escape>", lambda e: self.press("C"))

    def make_button(self, text, row, col, span=1):
        if text == "=":
            color = "#00ADB5"
        elif text in "C⌫":
            color = "#FF5722"
        elif text in "+-*/%":
            color = "#4B5563"
        else:
            color = "#393E46"

        btn = tk.Button(
            self,
            text=text,
            font=("Arial", 18),
            bg=color,
            fg="white",
            activebackground="#00ADB5",
            activeforeground="white",
            bd=0,
            width=4,
            height=2,
            command=lambda t=text: self.press(t),
        )
        btn.grid(row=row, column=col, columnspan=span, padx=4, pady=4, sticky="nsew")

    def on_key(self, event):
        if event.char and event.char in "0123456789.+-*/%":
            self.press(event.char)

    def press(self, key):
        if key == "C":
            self.expression = ""
            self.display_var.set("0")
        elif key == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression or "0")
        elif key == "=":
            self.calculate()
        else:
            self.expression += key
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            allowed = set("0123456789.+-*/% ")
            if not self.expression or not set(self.expression) <= allowed:
                raise ValueError
            result = eval(self.expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            self.expression = ""
            self.display_var.set("Cannot divide by 0")
        except Exception:
            self.expression = ""
            self.display_var.set("Error")


if __name__ == "__main__":
    Calculator().mainloop()