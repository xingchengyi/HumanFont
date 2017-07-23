'''
reg_all(canvas_object)
'''
import reg_font
import import_path

def reg_all(canvas_object):
    reg_test = canvas_object.beginText()
    reg_test.setTextOrigin(100,800)
    font_list,font_n=import_path.get_font_list()
    for fonts in font_list:
        rel_path = './fonts/' + fonts
        reg_font.reg_Fonts(rel_path,fonts)
        reg_test.setFont(fonts,25)
        reg_test.textLine(' ')
        canvas_object.drawText(reg_test)
