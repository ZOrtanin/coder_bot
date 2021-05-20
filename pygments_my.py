from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

def code2img(input_fileobj, output_fileobj):
    python_code = input_fileobj.read()
    png_code = highlight(python_code, PythonLexer(), ImageFormatter())
    output_fileobj.write(png_code)
    
if __name__ == "__main__":
    code2img(open("code2img.py"), open("code2img.png", "w"))