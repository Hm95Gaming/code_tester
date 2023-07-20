import tkinter as tk
from tkinter import scrolledtext
import sys
import io
import traceback

class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.configure(state="normal")
        self.text_widget.insert(tk.END, text)
        self.text_widget.configure(state="disabled")

def run_code():
    code = code_text.get("1.0", tk.END)
    output_text.configure(state="normal")
    output_text.delete("1.0", tk.END)
    try:
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        exec(code, globals(), locals())
        output = output_buffer.getvalue()
        output_text.insert(tk.END, output)
    except Exception as e:
        exception_str = str(e) + "\n\nTraceback:\n" + traceback.format_exc()
        output_text.insert(tk.END, exception_str)
    output_text.configure(state="disabled")

window = tk.Tk()
window.title("Code Tester")

code_text = scrolledtext.ScrolledText(window, width=50, height=10)
code_text.pack()

run_button = tk.Button(window, text="Run", command=run_code)
run_button.pack()

output_text = scrolledtext.ScrolledText(window, width=50, height=10)
output_text.pack()
output_text.configure(state="disabled")

window.mainloop()
