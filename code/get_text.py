def get_text(file_name):
    file_rel = './input/'+file_name
    fileobj = open(file_rel)
    strings = fileobj.read()
    fileobj.close()
    return strings

text=get_text('input.txt')
print text