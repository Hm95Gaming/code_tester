import subprocess
import webbrowser
import os
from contextlib import redirect_stdout
from io import StringIO

class CodeTester:
    def __init__(self):
        self.code_presets = {
            "Python": "print('Hello, World!')",
            "Java": "public class MyProgram {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
            "C++": "#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}",
            "PHP": "<?php\n    echo \"Hello, World!\";\n?>",
            "HTML": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Hello, World!</title>\n</head>\n<body>\n    <h1>Hello, World!</h1>\n</body>\n</html>"
        }

    def run_code(self, code, language):
        try:
            if language == "Python":
                output = StringIO()
                with redirect_stdout(output):
                    exec(code, globals(), globals())
                return output.getvalue().strip()
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
            elif language == "HTML":
                result = self.validate_html(code)
                print(result)
                if "valid" in result.lower():
                    self.show_html_output_in_browser(code)
                return result
        except Exception as e:
            return str(e)

    def validate_html(self, code):
        try:
            # We can use a library like BeautifulSoup to parse and validate HTML
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(code, "html.parser")
            return "HTML code is valid."
        except Exception as e:
            return "Invalid HTML code: " + str(e)


    def run_code_preset(self, language):
        if language in self.code_presets:
            code = self.code_presets[language]
            if language == "HTML":
                result = self.validate_html(code)
                print(result)
                if "valid" in result.lower():
                    self.show_html_output_in_browser(code)
                return result            
            else:
                return self.run_code(code, language)

    def detect_language(self, code):
        # Perform language detection here.
        # This is a simple example that checks for keywords unique to each language.
        if "def " in code or "print(" in code:
            return "Python"
        elif "public class" in code or "System.out.println" in code:
            return "Java"
        elif "#include" in code or "std::cout" in code:
            return "C++"
        elif "<?php" in code or "echo" in code:
            return "PHP"
        elif "<html" in code or "<body" in code:
            return "HTML"
        else:
            raise ValueError("Language detection failed. Please specify the language explicitly.")

    def run_code_auto(self, code):
        try:
            language = self.detect_language(code)
            return self.run_code(code, language)
        except Exception as e:
            return str(e)

    def show_html_output_in_browser(self, html_code):
        with open("output.html", "w") as file:
            file.write(html_code)

        if os.name == "nt":  # Windows
            try:
                url = "file://" + os.path.realpath("output.html")
                webbrowser.open(url)
            except FileNotFoundError:
                print("No browser found. Please open output.html manually.")
        elif os.name == "posix":  # Linux
            try:
                subprocess.run(["xdg-open", "output.html"], check=True)
            except FileNotFoundError:
                print("xdg-open command not found. Please open output.html manually.")


code_tester = CodeTester()
# Contoh menjalankan kode preset dan mencetak output ke konsol
#print(code_tester.run_code_preset("Python"))
#print(code_tester.run_code_preset("Java"))
#print(code_tester.run_code_preset("C++"))
#print(code_tester.run_code_preset("PHP"))

# Contoh penggunaan HTML di code tester
#code_tester.run_code("your_html_code_here", "HTML")
#code_tester.run_code_preset("HTML")

# Contoh menjalankan run_code_auto dan mencetak output ke konsol
#print(code_tester.run_code_auto("print('Hello, Auto Run!')"))

# versi kedua dari menjalankan run_code_auto
#php_code = "<?php\n    echo \"Hello, PHP World!\";\n?>"
#output_php = code_tester.run_code_auto(php_code)
#print(output_php)
