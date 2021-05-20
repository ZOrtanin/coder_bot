from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from pygments.styles import STYLE_MAP
from pygments.style import Style
from pygments.token import Token
from pygments.token import Keyword, Name, Comment, String, Error, \
    Literal, Number, Operator, Other, Punctuation, Text, Generic, \
    Whitespace

import os
import io
import PIL.Image as Image

from array import array

class MyStyle(Style):
    background_color = "#191919"
    default_style = ""

    styles = {
        Comment: "#6272a4",
        Comment.Hashbang: "#6272a4",
        Comment.Multiline: "#6272a4",
        Comment.Preproc: "#ff79c6",
        Comment.Single: "#6272a4",
        Comment.Special: "#6272a4",

        Generic: "#f8f8f2",
        Generic.Deleted: "#8b080b",
        Generic.Emph: "#f8f8f2 underline",
        Generic.Error: "#f8f8f2",
        Generic.Heading: "#f8f8f2 bold",
        Generic.Inserted: "#f8f8f2 bold",
        Generic.Output: "#44475a",
        Generic.Prompt: "#f8f8f2",
        Generic.Strong: "#f8f8f2",
        Generic.Subheading: "#f8f8f2 bold",
        Generic.Traceback: "#f8f8f2",

        Error: "#f8f8f2",

        Keyword: "#ff79c6",
        Keyword.Constant: "#ff79c6",
        Keyword.Declaration: "#8be9fd italic",
        Keyword.Namespace: "#ff79c6",
        Keyword.Pseudo: "#ff79c6",
        Keyword.Reserved: "#ff79c6",
        Keyword.Type: "#8be9fd",

        Literal: "#f8f8f2",
        Literal.Date: "#f8f8f2",

        Name: "#f8f8f2",
        Name.Attribute: "#50fa7b",
        Name.Builtin: "#8be9fd italic",
        Name.Builtin.Pseudo: "#f8f8f2",
        Name.Class: "#50fa7b",
        Name.Constant: "#f8f8f2",
        Name.Decorator: "#f8f8f2",
        Name.Entity: "#f8f8f2",
        Name.Exception: "#f8f8f2",
        Name.Function: "#50fa7b",
        Name.Label: "#8be9fd italic",
        Name.Namespace: "#f8f8f2",
        Name.Other: "#f8f8f2",
        Name.Tag: "#ff79c6",
        Name.Variable: "#8be9fd italic",
        Name.Variable.Class: "#8be9fd italic",
        Name.Variable.Global: "#8be9fd italic",
        Name.Variable.Instance: "#8be9fd italic",

        Number: "#bd93f9",
        Number.Bin: "#bd93f9",
        Number.Float: "#bd93f9",
        Number.Hex: "#bd93f9",
        Number.Integer: "#bd93f9",
        Number.Integer.Long: "#bd93f9",
        Number.Oct: "#bd93f9",

        Operator: "#ff79c6",
        Operator.Word: "#ff79c6",

        Other: "#f8f8f2",

        Punctuation: "#f8f8f2",

        String: "#f1fa8c",
        String.Backtick: "#f1fa8c",
        String.Char: "#f1fa8c",
        String.Doc: "#f1fa8c",
        String.Double: "#f1fa8c",
        String.Escape: "#f1fa8c",
        String.Heredoc: "#f1fa8c",
        String.Interpol: "#f1fa8c",
        String.Other: "#f1fa8c",
        String.Regex: "#f1fa8c",
        String.Single: "#f1fa8c",
        String.Symbol: "#f1fa8c",

        Text: "#f8f8f2",

        Whitespace: "#f8f8f2"

    }

def code2img(input_fileobj, output_fileobj):
    python_code = input_fileobj
    png_code = highlight(python_code, PythonLexer(), ImageFormatter(
        font_size=20,
        style=MyStyle,
        line_number_bg='#191919',
        line_number_fg = '#697187',
        line_number_separator=False
        ))

    image = Image.open(io.BytesIO(png_code))
    print(image.size)
    image.save('code2img2.jpg')

    
if __name__ == "__main__":
    code = '''
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

import os
import io
import PIL.Image as Image

from array import array

def code2img(input_fileobj, output_fileobj):
    python_code = input_fileobj
    png_code = highlight(python_code, PythonLexer(), ImageFormatter(font_size=20))
    #print(png_code)
    #output_fileobj.write(str(png_code))

    image = Image.open(io.BytesIO(png_code))
    image.save('code2img2.jpg')
    '''

    code2img(code, open("code2img.png", "w"))