from reportlab.pdfgen.canvas import Canvas
import reg_font
relpath = r".\fonts\font_1.ttf"
reg_font.reg_Fonts(relpath,'font_1')
output_files = r".\output\output.pdf"
pdf  = Canvas(output_files)
y=800
pdf_file = open(r".\input\input.in",'r')
pdf.setFont('font_1',20)
lines = pdf_file.readlines()
for line in lines:
    pdf.drawString(100,y,line.strip())
    y-=20
pdf.save()