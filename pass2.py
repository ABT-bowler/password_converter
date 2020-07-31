from tkinter import *
import tkinter.messagebox

HEIGHT = 400
WIDTH = 700

root = Tk()
root.title("Title Goes Here")

a_canvas = Canvas(root, height=HEIGHT, width=WIDTH)
a_canvas.pack()


# sample_input_pass = "Samp!e1"


# Lines 16-23 worked for one letter at a time
def clicked():
    entered = a_entry.get()
    a_textbox.delete(0.0, END)
    try:
        textin = ", ".join(loop_over_input(entered))
    except:
        textin = 'Sorry invalid information provided.\nResubmit with the correct information.\n'
    a_textbox.insert(0.0, textin)


def clr():
    a_entry.set(" ")


def gone():
    tkinter.messagebox.showinfo("Program", 'Exit')
    exit()


# Keep this is the master code
def loop_over_input(the_str=''):
    master_list = []
    for char in the_str:
        tmp_char = passwordConversion[char]
        master_list.append(tmp_char)
    print("Master Pass List: ", master_list)
    return master_list


def cont():
    tkinter.messagebox.showinfo("About",
                                '\n Wrote by Sean \n Version 1.0 \n Python\Tkinter')


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
    "|": "pipe",
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


a_frame = Frame(root, bg='Red', bd=5)
a_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

a_middle_frame = Frame(root, bg='White')
a_middle_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.25, anchor='n')

# a_lower_frame = Frame(root, bg='White', bd=10)
# a_lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.25, anchor='n')


# Creating entry boxes
a_entry = Entry(a_frame, font=20)
a_entry.place(relwidth=0.65, relheight=1)

# a_entry2 = Entry(a_lower_frame, font=40)
# a_entry2.place(relwidth=1.00, relheight=1.00)


# Create a text box
a_textbox = Text(a_middle_frame, font=12)
a_textbox.place(relwidth=1.00, relheight=1)

# Creating button
a_button = Button(a_frame, padx=2, pady=2, text='Convert Password', command=clicked, bg='Green', font=('none 11 bold'))
a_button.place(relx=0.7, relheight=1, relwidth=0.3)

a_button2 = Button(root, padx=2, pady=2, text='Clear', font=('none 18 bold'), bg='Red', command=clr)
a_button2.pack()

a_button3 = Button(root, padx=2, pady=2, text='Exit', command=gone, bg='Yellow', font=('none 18 bold'))
a_button3.place(x=200, y=470)

a_label = Label(text="- Disclaimer - \n- Disclaimer line 2 -", )
a_label.pack(side='bottom')

# Define Menu Items
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Create another submenu Edit
edit_menu = Menu(my_menu)
# my_menu.add_cascade(label="About", menu=edit_menu)
my_menu.add_command(label="About", command=cont)

root.mainloop()

