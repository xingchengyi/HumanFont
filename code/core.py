
# -*- coding: utf-8 -*-
from reportlab.pdfgen.canvas import Canvas
import random
import reg_all_Fonts
import import_path
def core(output_file_,input_texts,font_size):
    output_file_name = output_file_
    output_file = './output/'+output_file_name
    output_canvas = Canvas(output_file)
    size=font_size
    input_text=input_texts
    input_len = len(input_text)

    reg_all_Fonts.reg_all(output_canvas)
    fonts_list,fonts_n=import_path.get_font_list()


    ori_x=100
    ori_y=800
    x=ori_x
    y=ori_y

    output_canvas.setPageSize([600,850])
    split_size = size * 0.5
    split_size= int(split_size)

    max_x = (600-(2*x))/split_size
    max_y = ((2*y) - 850)/size

    count_x=0
    count_y=0


    for each_char in range(input_len):
        random_font = fonts_list[random.randint(0,fonts_n-1)]
        output_canvas.setFont(random_font,size)
        sp_char=input_text[each_char]

        if count_y == max_y and count_x >= max_x :
            output_canvas.showPage()
            output_canvas.setPageSize([600, 850])
            random_font = fonts_list[random.randint(0, fonts_n - 1)]
            output_canvas.setFont(random_font, size)
            y = ori_y
            x = ori_x
            count_y = 1
            count_x = 1
            output_canvas.drawString(x, y,sp_char)
            x+=split_size

        elif count_y == max_y and sp_char == '\n':
            output_canvas.showPage()
            output_canvas.setPageSize([600, 850])
            random_font = fonts_list[random.randint(0, fonts_n - 1)]
            output_canvas.setFont(random_font, size)
            y = ori_y
            x = ori_x
            count_y = 0
            count_x = 0
            output_canvas.drawString(x, y, sp_char)


        elif count_y <> max_y and sp_char == '\n':
            y-=size
            x=ori_x
            count_x=1
            count_y +=1
            output_canvas.drawString(x, y,sp_char)

        elif count_x >= (max_x+1):
            y-=size
            x=ori_x
            count_y+=1
            count_x=1
            output_canvas.drawString(x, y,sp_char)
            x+=split_size

        else:
            if sp_char==' ':
                x+=(split_size*2)
                count_x+=2
            else:
                output_canvas.drawString(x, y, sp_char)
                x += split_size
                count_x += 1

    output_canvas.save()