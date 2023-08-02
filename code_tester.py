import subprocess
import webbrowser
import os
import php
import threading
import http.server
import socketserver
import time
from contextlib import redirect_stdout
from io import StringIO
from bs4 import BeautifulSoup

class CodeTester:
    def __init__(self):
        # var untuk set Html
        self.php_code = None
        self.html_code = None
        self.css_code = None
        self.js_code = None
        
        # Kode presets untuk berbagai bahasa pemrograman
        self.code_presets = {
            "Python": "print('Hello, World!')",
            "Java": "public class MyProgram {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
            "C++": "#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}",
            "PHP": "<?php\n    echo 'Hello, World!';\n?>",
            "HTML": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Hello, World!</title>\n</head>\n<body>\n    <h1>Hello, World!</h1>\n</body>\n</html>",
            "CSS": "body { background-color: #1ecbe1; color: #333; font-family: Arial, sans-serif; } h1 { color: #04AA6D; }",
            "JavaScript": "alert('Hello, World!');"
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
                if "valid" in result.lower():
                    self.show_html_output_in_browser(code)
                return result
            elif language == "CSS":
                return self.execute_css(code)
            elif language in ["JS","JavaScript"]:
                return self.execute_javascript(code)
            else:
                raise ValueError("Language not supported.")
        except Exception as e:
            return str(e)

    def validate_html(self, code):
        try:
            # We can use a library like BeautifulSoup to parse and validate HTML
            soup = BeautifulSoup(code, "html.parser")
            return "HTML code is valid."
        except Exception as e:
            return "Invalid HTML code: " + str(e)

    def execute_css(self, code):
        try:
            self.create_html_page_with_css(code)
            return "CSS code executed successfully:\n" + code
        except Exception as e:
            return "Failed to execute CSS code: " + str(e)

    def execute_javascript(self, code):
        try:
            # Eksekusi kode JavaScript
            self.create_html_page_with_javascript(code)
            return "JavaScript code executed successfully:\n" + code
        except Exception as e:
            return "Failed to execute JavaScript code: " + str(e)

    def create_html_page_with_css(self, css_code):
        html_code = f"""<!DOCTYPE html>
<html>
<head>
    <title>CSS Code Test</title>
    <style>
        {css_code}
    </style>
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
</body>
</html>"""

        with open("output.html", "w") as file:
            file.write(html_code)

        # Buka file HTML di browser
        url = "file://" + os.path.realpath("output.html")
        webbrowser.open(url)

    def create_html_page_with_javascript(self, js_code):
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>JavaScript Output</title>
            <script>
                function runCode() {{
                    {js_code}
                }}
            </script>
        </head>
        <body>
            <h1>JavaScript Output</h1>
            <button onclick="runCode()">Click to Run JavaScript</button>
        </body>
        </html>
        """

        with open("output.html", "w") as file:
            file.write(html_code)

        # Buka file HTML di browser
        url = "file://" + os.path.realpath("output.html")
        webbrowser.open(url)

    def run_code_preset(self, language):
        if language in self.code_presets:
            code = self.code_presets[language]
            if language == "HTML":
                result = self.validate_html(code)
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
        elif "body" in code and "{" in code and "}" in code and ":" in code:
            return "CSS"
        elif "console.log(" in code or "function " in code or "var " in code or "const " in code or "alert(" in code:
            return "JavaScript"
        else:
            raise ValueError("Language detection failed. Please specify the language explicitly.")

    def run_code_auto(self, code):
        try:
            language = self.detect_language(code)
            return self.run_code(code, language)
        except Exception as e:
            return str(e)

    def show_html_output_in_browser(self, html_code):
        # Save the HTML code to a temporary file
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


    def html_set(self, *args):
        code = self.detect_language(args[0])
        php_code = None
        html_code = None
        css_code = None
        js_code = None

        if code == "PHP":
            php_code = args[0]
            html_code = args[1]
            if len(args) >= 3:
                code3 = self.detect_language(args[2])
                if code3 == "CSS":
                    css_code = args[2]
                    if len(args) >= 4 and args[3] != "":
                        js_code = args[3]
                        return self.build_html_set(php_code,html_code,css_code,js_code)
                    else:
                        return self.build_html_set(php_code,html_code,css_code,js_code)
                elif code3 == "JS" or code3 == "JavaScript":
                    js_code = args[2]
                    if len(args) >= 4 and args[3] != "":
                        css_code = args[3]
                        return self.build_html_set(php_code,html_code,css_code,js_code)
                    else:
                        return self.build_html_set(php_code,html_code,css_code,js_code)
            else:
                return self.build_html_set(php_code,html_code,css_code,js_code)
        elif code == "HTML":
            html_code = args[0]
            code2 = self.detect_language(args[1])
            if code2 == "CSS":
                css_code = args[1]
                if len(args) >= 3 and args[2] != "":
                    js_code = args[2]
                    return self.build_html_set(php_code,html_code,css_code,js_code)
                else:
                    return self.build_html_set(php_code,html_code,css_code,js_code)
            elif code2 == "JavaScript":
                js_code = args[1]
                if len(args) >= 3 and args[2] != "":
                    css_code = args[2]
                    return self.build_html_set(php_code,html_code,css_code,js_code)
                else:
                    return self.build_html_set(php_code,html_code,css_code,js_code)
            else:
                raise ValueError("Maaf code css atau js tidak ditemukan")
        else:
            raise ValueError("Maaf code harus sesuai urutan 1.php 2.html 3.css 4.js atau 1.html 2.css 3.js Note: css dan js bisa tebalik")

    def extract_html_head_and_body(self, html_code):
        try:
            # Parse the HTML code using BeautifulSoup
            soup = BeautifulSoup(html_code, "html.parser")

            # Find the head and body elements
            head_element = soup.find("head")
            body_element = soup.find("body")

            # Extract the code for head and body
            head_code = str(head_element) if head_element else ""
            body_code = str(body_element) if body_element else ""

            return head_code, body_code
        except Exception as e:
            return None, None

    def build_html_set(self, php_code, html_code, css_code, js_code):
        if php_code != None:
            head_code, body_code = self.extract_html_head_and_body(html_code)
            if css_code != None:
                soup = BeautifulSoup(head_code, "html.parser")
                style_element = soup.new_tag("style")
                style_element.string = css_code
                soup.head.append(style_element)
                head_code = str(soup.head)
                if js_code != None:
                    soup = BeautifulSoup(body_code, "html.parser")
                    script_element = soup.new_tag("script")
                    script_element.string = js_code
                    soup.body.append(script_element)
                    body_code = str(soup.body)
                    code_set = f"""
                        {php_code}
                        <!DOCTYPE html>
                        <html>
                            {head_code}
                            {body_code}
                        </html>
                    """

                    htdocs_path = "C:/xampp/htdocs"
                    output_file_path = os.path.join(htdocs_path, "output.php")
                    with open(output_file_path, "w") as file:
                        file.write(code_set)
                    url = "http://localhost/output.php"
                    webbrowser.open(url)
                else:
                    code_set = f"""
                        {php_code}
                        <!DOCTYPE html>
                        <html>
                            {head_code}
                            {body_code}
                        </html>
                    """

                    htdocs_path = "C:/xampp/htdocs"
                    output_file_path = os.path.join(htdocs_path, "output.php")
                    with open(output_file_path, "w") as file:
                        file.write(code_set)
                    url = "http://localhost/output.php"
                    webbrowser.open(url)
            elif js_code != None:
                soup = BeautifulSoup(body_code, "html.parser")
                script_element = soup.new_tag("script")
                script_element.string = js_code
                soup.body.append(script_element)
                body_code = str(soup.body)
                code_set = f"""
                    {php_code}
                    <!DOCTYPE html>
                    <html>
                        {head_code}
                        {body_code}
                    </html>
                """

                htdocs_path = "C:/xampp/htdocs"
                output_file_path = os.path.join(htdocs_path, "output.php")
                with open(output_file_path, "w") as file:
                    file.write(code_set)
                url = "http://localhost/output.php"
                webbrowser.open(url)
            else:
                code_set = f"""
                    {php_code}
                    <!DOCTYPE html>
                    <html>
                        {head_code}
                        {body_code}
                    </html>
                """

                htdocs_path = "C:/xampp/htdocs"
                output_file_path = os.path.join(htdocs_path, "output.php")
                with open(output_file_path, "w") as file:
                    file.write(code_set)
                url = "http://localhost/output.php"
                webbrowser.open(url)

        else:
            head_code, body_code = self.extract_html_head_and_body(html_code)
            if css_code != None:
                soup = BeautifulSoup(head_code, "html.parser")
                style_element = soup.new_tag("style")
                style_element.string = css_code
                soup.head.append(style_element)
                head_code = str(soup.head)
                if js_code != None:
                    soup = BeautifulSoup(body_code, "html.parser")
                    script_element = soup.new_tag("script")
                    script_element.string = js_code
                    soup.body.append(script_element)
                    body_code = str(soup.body)
                    code_set = f"""
                        <!DOCTYPE html>
                        <html>
                            {head_code}
                            {body_code}
                        </html>
                    """

                    htdocs_path = "C:/xampp/htdocs"
                    output_file_path = os.path.join(htdocs_path, "output.php")
                    with open(output_file_path, "w") as file:
                        file.write(code_set)
                    url = "http://localhost/output.php"
                    webbrowser.open(url)
                else:
                    code_set = f"""
                        <!DOCTYPE html>
                        <html>
                            {head_code}
                            {body_code}
                        </html>
                    """

                    htdocs_path = "C:/xampp/htdocs"
                    output_file_path = os.path.join(htdocs_path, "output.php")
                    with open(output_file_path, "w") as file:
                        file.write(code_set)
                    url = "http://localhost/output.php"
                    webbrowser.open(url)
            elif js_code != None:
                soup = BeautifulSoup(body_code, "html.parser")
                script_element = soup.new_tag("script")
                script_element.string = js_code
                soup.body.append(script_element)
                body_code = str(soup.body)
                code_set = f"""
                    <!DOCTYPE html>
                    <html>
                        {head_code}
                        {body_code}
                    </html>
                """

                htdocs_path = "C:/xampp/htdocs"
                output_file_path = os.path.join(htdocs_path, "output.php")
                with open(output_file_path, "w") as file:
                    file.write(code_set)
                url = "http://localhost/output.php"
                webbrowser.open(url)
            else:
                code_set = f"""
                    <!DOCTYPE html>
                    <html>
                        {head_code}
                        {body_code}
                    </html>
                """

                htdocs_path = "C:/xampp/htdocs"
                output_file_path = os.path.join(htdocs_path, "output.php")
                with open(output_file_path, "w") as file:
                    file.write(code_set)
                url = "http://localhost/output.php"
                webbrowser.open(url)
        

code_tester = CodeTester()
# Contoh menjalankan kode preset dan mencetak output ke konsol
#print(code_tester.run_code_preset("Python"))
#print(code_tester.run_code_preset("Java"))
#print(code_tester.run_code_preset("C++"))
#print(code_tester.run_code_preset("PHP"))

# Contoh penggunaan HTML di code tester
#code_tester.run_code("your_html_code_here", "HTML")
#code_tester.run_code_preset("HTML")
#code_tester.run_code_auto("<!DOCTYPE html><html><head><title>Contoh Halaman HTML</title><link rel='stylesheet' href='style.css'><script src='script.js'></script></head><body><header><h1>Selamat Datang di Contoh Halaman HTML</h1><nav><ul><li><a href='#home'>Beranda</a></li><li><a href='#about'>Tentang Kami</a></li><li><a href='#contact'>Kontak</a></li></ul></nav></header><main><section id='home'><h2>Selamat datang di Beranda</h2><p>Ini adalah halaman beranda contoh.</p></section><section id='about'><h2>Tentang Kami</h2><p>Kami adalah sebuah perusahaan fiksi yang mengembangkan solusi web inovatif.</p></section><section id='contact'><h2>Kontak</h2><p>Jika Anda memiliki pertanyaan, silakan hubungi kami di email@example.com.</p></section></main><footer><p>Hak Cipta &copy; 2023 Nama Perusahaan. Seluruh hak cipta dilindungi.</p></footer></body></html>")
#code_tester.run_code_auto('<!DOCTYPE html><html><head><title>Contoh Halaman Web dengan Sidebar Navigasi</title><style>.sidebar{margin:0;padding:0;width:200px;background-color:#f1f1f1;position:fixed;height:100%;overflow:auto;}.sidebar a{display:block;color:black;padding:16px;text-decoration:none;}.sidebar a.active{background-color:#04AA6D;color:white;}.sidebar a:hover:not(.active){background-color:#555;color:white;}.content{margin-left:200px;padding:1px 16px;height:1000px;}.sidebar{width:100%;height:auto;position:relative;}.sidebar a{float:left;}.content{margin-left:0;}}@media screen and (max-width:700px){.sidebar{width:100%;height:auto;position:relative;}.sidebar a{float:left;}.content{margin-left:0;}}@media screen and (max-width:400px){.sidebar a{text-align:center;float:none;}}</style></head><body><div class="sidebar"><a href="#" class="active">Beranda</a><a href="#">Tentang</a><a href="#">Kontak</a><a href="#">Layanan</a></div><div class="content"><h1>Selamat Datang di Halaman Web</h1><p>Ini adalah contoh halaman web sederhana dengan sidebar navigasi.</p><p>Anda dapat menambahkan lebih banyak konten di sini.</p></div></body></html>')


# Contoh menjalankan run_code_auto dan mencetak output ke konsol
#print(code_tester.run_code_auto("print('Hello, Auto Run!')"))

# versi kedua dari menjalankan run_code_auto
#php_code = "<?php\n    echo \"Hello, PHP World!\";\n?>"
#output_php = code_tester.run_code_auto(php_code)
#print(output_php)

# Contoh penggunaan CSS di code tester
#print(code_tester.run_code("body { background-color: #1ecbe1; color: #333; }", "CSS"))
#print(code_tester.run_code_auto('body { background-color: #f1f1f1; color: #333; } h1 { color: blue; }'))

#Contoh penggunaan JS di code tester
#print(code_tester.run_code_auto("alert('Hello, World!');"))
#print(code_tester.run_code_auto('const message = "Hello, World!"; console.log(message); function addNumbers(a, b) { return a + b; } const result = addNumbers(5, 10); console.log(result); alert("This is an alert!");'))

# Contoh penggunaan set HTML
php_code = "<?php echo 'Hello, PHP!'; ?>"
html_code = "<html><head><title>hello</title></head><body><p>Halo orang Gabut!</p></body></html>"
css_code = "body { background-color: lightblue; }"
js_code = "alert('Hello, JavaScript!');"
code_tester.html_set(html_code, js_code)
