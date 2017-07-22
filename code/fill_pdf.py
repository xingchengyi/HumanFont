#-*-coding: utf-8-*-
from reportlab.pdfgen.canvas import Canvas
import reportlab.pdfgen as rp
import reg_font
relpath = r".\fonts\font_1.ttf"
reg_font.reg_Fonts(relpath,'font_1')
output_files = r".\output\temp.pdf"
canv = Canvas(output_files)
text_t = canv.beginText()
text_t.setTextOrigin(50,800)
text_t.setFont('font_1',10)
text_t.textLines('''
    h e l l o w o r l f
    s d
    a d s f f a d s
    s a d d a s f a d a d s f a d f f d a s
    sdadsaffddafsadfdfasjk;adsfjkl;
    asdioeqwruoeqwrfdasjkadsffdasjkdasfjkadsfjkjadsfkjadsfkdasfjk;dasfjkadsfjjdsfkdfsjkdsfjk;
    adsfjkladsfjkadsfjjadsfdasfjkdsafjkldasfjkldasfjkl;
    adsfdasfkjlsadfjfadsj
    fadjk;dafjkl;adsfjkl;
    fadsjkladsfjkl;jkladf
    sadfjk;adsfjkladsfjk
    adsfjkl'
    \n
    ';;;;;;;;;;;;;;;;;;;;;;;;;;kjl;kjl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
''')
canv.drawText(text_t)
canv.save()
for font in canv.getAvailableFonts():
    print font