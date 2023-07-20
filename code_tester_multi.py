import tkinter as tk
from tkinter import scrolledtext
import sys
import io
import traceback
import subprocess
import os

class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.configure(state="normal")
        self.text_widget.insert(tk.END, text)
        self.text_widget.configure(state="disabled")

# Preset kode untuk setiap bahasa
code_presets = {
    "Python": "print('Hello, World!')",
    "Java": "public class MyProgram {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
    "C++": "#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}",
    "PHP": "<?php\n    echo \"Hello, World!\";\n?>"
}

class CodeTester:
    def __init__(self):
        self.code_presets = code_presets

    def get_preset_code(self, language):
        if language in self.code_presets:
            return self.code_presets[language]
        return ""

    def run_code(self, code, language):
        try:
            if language == "Python":
                output_buffer = io.StringIO()
                sys.stdout = output_buffer
                exec(code, globals(), globals())
                sys.stdout = sys.__stdout__  # Mengembalikan stdout ke konsol
                return output_buffer.getvalue()
            elif language == "Java":
                with open("MyProgram.java", "w") as file:
                    file.write(code)
                process = subprocess.Popen(["javac", "MyProgram.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()
                if stderr:
                    return "\n\nCompilation Error:\n" + stderr
                else:
                    process = subprocess.Popen(["java", "MyProgram"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    stdout, stderr = process.communicate()
                    output = stdout
                    if stderr:
                        output += "\n\nRuntime Error:\n" + stderr
                    os.remove("MyProgram.java")  # Menghapus file Java setelah selesai
                    os.remove("MyProgram.class")  # Menghapus file bytecode Java setelah selesai
                    return output
            elif language == "C++":
                with open("MyProgram.cpp", "w") as file:
                    file.write(code)
                process = subprocess.Popen(["g++", "MyProgram.cpp", "-o", "MyProgram"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()
                if stderr:
                    return "\n\nCompilation Error:\n" + stderr
                else:
                    process = subprocess.Popen(["./MyProgram"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    stdout, stderr = process.communicate()
                    output = stdout
                    if stderr:
                        output += "\n\nRuntime Error:\n" + stderr
                    os.remove("MyProgram.cpp")  # Menghapus file C++ setelah selesai
                    return output
            elif language == "PHP":
                with open("code.php", "w") as file:
                    file.write(code)
                process = subprocess.Popen(["php", "code.php"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()
                output = stdout
                if stderr:
                    output += "\n\nError:\n" + stderr
                os.remove("code.php")  # Menghapus file PHP setelah selesai
                return output
        except Exception:
            exception_str = traceback.format_exc()
            sys.stdout = sys.__stdout__  # Mengembalikan stdout ke konsol
            return exception_str

def run_code():
    code = code_text.get("1.0", tk.END)
    output_text.configure(state="normal")
    output_text.delete("1.0", tk.END)
    language = language_var.get()
    code_tester = CodeTester()
    output = code_tester.run_code(code, language)
    output_text.insert(tk.END, str(output))
    output_text.configure(state="disabled")

def change_language(*args):
    language = language_var.get()
    code_tester = CodeTester()
    preset_code = code_tester.get_preset_code(language)
    code_text.delete("1.0", tk.END)
    code_text.insert(tk.END, preset_code)
    update_line_number()

def update_line_number(*args):
    line_number.configure(state="normal")
    line_number.delete("1.0", tk.END)
    code_lines = code_text.get("1.0", tk.END).count("\n")
    line_number.insert(tk.END, "\n".join(str(i+1) for i in range(code_lines + 1)))
    line_number.configure(state="disabled")

    # Scroll line number secara otomatis mengikuti scroll teks masukan
    line_number.yview_moveto(code_text.yview()[0])

window = tk.Tk()
window.title("Code Tester")

# Membuat frame untuk teks masukan dan line number
input_frame = tk.Frame(window)
input_frame.pack(side="top", pady=10)

# Membuat teks masukan
code_text = scrolledtext.ScrolledText(input_frame, width=50, height=10)
code_text.pack(side="left", padx=10)

# Membuat teks line number
line_number = scrolledtext.ScrolledText(input_frame, width=5, height=10)
line_number.pack(side="left", padx=(0, 10))
line_number.insert(tk.END, "1")

code_text.bind("<KeyPress>", update_line_number)
code_text.bind("<KeyRelease>", update_line_number)

# Membuat frame untuk tombol "Run" dan radio bahasa
button_frame = tk.Frame(window)
button_frame.pack(side="top", pady=5)

# Membuat tombol "Run"
run_button = tk.Button(button_frame, text="Run", command=run_code)
run_button.pack(side="left", padx=5)

# Membuat drop-down menu untuk memilih bahasa
language_var = tk.StringVar()
language_var.set("Python")
language_options = list(code_presets.keys())
language_menu = tk.OptionMenu(button_frame, language_var, *language_options, command=change_language)
language_menu.pack(side="left", padx=5)

# Memasukkan preset kode ke dalam teks masukan
change_language()

# Membuat frame untuk teks output
output_frame = tk.Frame(window)
output_frame.pack(side="top", pady=10)

# Membuat teks output
output_text = scrolledtext.ScrolledText(output_frame, width=50, height=10)
output_text.pack(side="bottom", padx=10)

output_text.configure(state="disabled")

window.mainloop()
