# -*- coding: utf-8 -*-
def get_text(file_name):
    file_name_str=str(file_name)
    file_rel = './input/'+file_name_str
    fileobj = open(file_rel)
    strings = fileobj.read()
    fileobj.close()
    return strings