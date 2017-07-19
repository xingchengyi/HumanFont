import reportlab.pdfbase.ttfonts
import reportlab.lib.fonts
#from reportlab.pdfgen import canvas
#from reportlab.lib.units import inch
def reg_Fonts(rel_path,fonts_name):
    rf = reportlab.pdfbase.ttfonts.pdfmetrics.registerFont
    rt = reportlab.pdfbase.ttfonts.TTFont
    rf(rt(fonts_name, rel_path))

#    outputs = ".\output\\"+output_pdf_file
#    pic = canvas.Canvas(outputs)
#    pic.setFont(fonts_name,25)
#    text_temp = pic.beginText(inch,inch*11)
#    text_temp.textOut(text)
#    pic.drawText(text_temp)
#    pic.showPage()
#    pic.save()
