from reportlab.pdfgen.canvas import Canvas
import reg_font
relpath = r".\fonts\font_1.ttf"
reg_font.reg_Fonts(relpath,'font_1')
pdf  = Canvas('temp.pdf')
y=800
pdf_file = open(r".\input\input.in",'r')
#for line in file(r".\input\input.in",'r'):
#   pdf.drawString(100,y,line.strip())
pdf.setFont('font_1',20)
pdf_data = pdf.getpdfdata()
print pdf_data
lines = pdf_file.readlines(1000)
for line in lines:
    pdf.drawString(100,y,line.strip())
    y-=20
pdf.save()