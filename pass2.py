#This file in incomplete and does not work as designed. 

from tkinter import *

HEIGHT = 400
WIDTH = 600

# sample_input_pass = "Samp!e1"

# Trying this
master_list = []
the_str = []


def loop_over_input(the_str=''):
    for char in the_str:
        tmp_char = passwordConversion[char]
        master_list.append(tmp_char)
    print("Master Pass List: ", master_list)
    return master_list


def clk():
    global the_str
    global master_list
    entered = ent.get()
    output.delete(0.0, END)
    for char in the_str:
        tmp_char = passwordConversion[char]
        master_list.append(tmp_char)
    print("Master Pass List ", master_list)
    return master_list
    output.insert(0.0, entry2)
    entry2 = passwordConversion[entered]


# Keep this is the master code
# def loop_over_input(the_str=''):
#     master_list = []
#     for char in the_str:
#         tmp_char = passwordConversion[char]
#         master_list.append(tmp_char)
#     print("Master Pass List: ", master_list)
#     return master_list

# Custom Dictionary
passwordConversion = {
    "A": "ALPHA",
    "a": "alpha",
    "B": "BRAVO",
    "b": "bravo",
    "C": "CHARLIE",
    "c": "charlie",
    "D": "DELTA",
    "d": "delta",
    "E": "ECHO",
    "e": "echo",
    "F": "FOXTROT",
    "f": "foxtrot",
    "G": "GOLF",
    "g": "golf",
    "H": "HOTEL",
    "h": "hotel",
    "I": "INDIA",
    "i": "india",
    "J": "JULIET",
    "j": "juliet",
    "K": "KILO",
    "k": "kilo",
    "L": "LIMA",
    "l": "lima",
    "M": "MIKE",
    "m": "mike",
    "N": "NOVEMBER",
    "n": "november",
    "O": "OSCAR",
    "o": "oscar",
    "P": "PAPA",
    "p": "papa",
    "Q": "QUEBEC",
    "q": "quebec",
    "R": "ROMEO",
    "r": "romeo",
    "S": "SIERRA",
    "s": "sierra",
    "T": "TANGO",
    "t": "tango",
    "U": "UNIFORM",
    "u": "uniform",
    "V": "VICTOR",
    "v": "victor",
    "W": "WHISKEY",
    "w": "whiskey",
    "X": "XRAY",
    "x": "xray",
    "Y": "YANKEE",
    "y": "yankee",
    "Z": "ZULU",
    "z": "zulu",
    "1": "Number 1",
    "2": "Number 2",
    "3": "Number 3",
    "4": "Number 4",
    "5": "Number 5",
    "6": "Number 6",
    "7": "Number 7",
    "8": "Number 8",
    "9": "Number 9",
    "0": "Number 0",
    "~": "tilde",
    "`": "back Quote",
    "!": "exclamation point",
    "@": "at sign",
    "#": "number sign",
    "$": "dollar sign",
    "%": "percent sign",
    "^": "caret",
    "&": "ampersand",
    "*": "asterisk",
    "(": "left parentheses",
    ")": "right parentheses",
    "_": "underscore",
    "-": "hyphen",
    "+": "plus sign",
    "=": "equals sign",
    "[": "left square bracket",
    "]": "right square bracket",
    "{": "left curly bracket",
    "}": "right curly bracket",
    #   "\": "backslash",
    "/": "forwardslash",
    #    "|": "pipe",
    "<": "less than sign",
    ">": "greater than sign",
    ",": "comma",
    ".": "peorid",
    "?": "question mark",
    ":": "colon",
    ";": "semicolon",
    '"': "double quote",
    "'": "single quote",

}

# loop_over_input(the_str=sample_input_pass)

root = Tk()
root.title("Title Goes Here")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg='Red', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.25, anchor='n')

entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

entry2 = Entry(lower_frame, font=40)
entry2.place(relwidth=1.00, relheight=1.00)

button = Button(frame, text="Password", font=40, )
button.place(relx=0.7, relheight=1, relwidth=0.3)

label = Label(text="- Disclaimer - \n- Disclaimer line 2 -", )
label.pack(side='bottom')

# Define Menu Items
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Create another submenu Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="About", menu=edit_menu)

root.mainloop()

# password = input("Please enter the password: ")

# print(passwordConversion)

