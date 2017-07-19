import os
def get_font_list():
    fonts_list = []
    fonts_times = 0
    for s in os.listdir(r'.\fonts'):
        fonts_list.append(s)
        fonts_times = fonts_times+1
    return fonts_list,fonts_times


