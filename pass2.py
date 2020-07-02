import tkinter as tk

HEIGHT = 700
WIDTH = 800

root =tk.Tk()

root.title("Put title here")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


def loop_over_input(the_str=''):
    master_list = []
    for char in the_str:
        tmp_char = passwordConversion[char]
        master_list.append(tmp_char)
    print("Master Pass List: ", master_list)
    return master_list

def click():
    entered = ent.get()
    output.delete(0.0,end)

frame = tk.Frame(root, bg='red', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Convert Password", font=40)
button.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame = tk.Frame(root, bg= 'gray', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label2 = tk.Label(root, text="Enter password to be converted", bg='white')
#label2.pack(side='top')

label1 = tk.Label(lower_frame, text="Disclamer goes here", bg='white')
label1.pack(side='bottom')



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
    "/": "forwardslash",
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

#password = input("Please enter the password: ")

#print(passwordConversion)

root.mainloop()


