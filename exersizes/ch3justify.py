# Right justify a string to column 70 of the screen

def rightjustify(sig):
    full_line = ""
    num_chars = len(sig)
    blank = 70 - num_chars
    full_line += " "*blank + sig
    pass
    print(full_line)

rightjustify("monty")
