import reportlab.pdfbase.ttfonts
import reportlab.lib.fonts
def reg_Fonts(rel_path,fonts_name):
    rf = reportlab.pdfbase.ttfonts.pdfmetrics.registerFont
    rt = reportlab.pdfbase.ttfonts.TTFont
    rf(rt(fonts_name, rel_path))
