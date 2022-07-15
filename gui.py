

from tkinter import *
from main import tts
import os
import re

# get names and titles of voices from main.py
with open("main.py", "r") as mainfile:
    lines = mainfile.readlines()

if not os.path.isdir('output'):
    os.mkdir('output')

print(lines[62])
voices_dict = {}
voice_title_list = []
for line in lines[12:61]:
    regex_search = re.search(r"'(.*?)'.*# (.*)", line)
    if regex_search:
        voice_name = regex_search.group(1)  # actual API name
        voice_title = regex_search.group(2)  # nice natural name
        voices_dict[voice_title] = voice_name
        voice_title_list.append(voice_title)


def run():
    voice = voices_dict[dropdown_var.get()]
    text = text_field.get("1.0", "end-1c")
    only_play = check_button_var.get()
    filename = filename_field.get("1.0", "end-1c")
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output', f"{filename}.mp3")
    filepath = os.path.join('output', f"{filename}.mp3")

    tts(voice, text, filepath, only_play)

    # set label
    if not only_play:
        after_run_label.configure(text=f"File saved at\n{filepath}")


w = Tk()
w.title('Tiktok Text-to-Speech')
w.geometry("500x400")

l = Label(
    w,
    text='Select a voice'
)
l.pack()

# Dropdown menu for voice *************
# datatype of menu text
dropdown_var = StringVar()
# initial menu text
dropdown_var.set(voice_title_list[10])
drop = OptionMenu(w, dropdown_var, *voice_title_list)
drop.pack()

# Text box for voiced text ************
# Create label
l = Label(w, text="Write text below")
l.pack()

# Create text widget and specify size.
text_field = Text(w, height=4, width=30)
text_field.config(font=("Calibri", 14))
text_field.pack()
default_text = "I'm walking here"
text_field.insert(END, default_text)
text_field.pack()

# Text box for filename ***************
# Create label
l = Label(w, text="Write filename below")
l.pack()

# Create text widget and specify size.
filename_field = Text(w, height=1, width=20)
filename_field.config(font=("Calibri", 12))
filename_field.pack()
default_filename = "text-to-speech"
filename_field.insert(END, default_filename)
filename_field.pack()


# Check button for playing ************
check_button_var = BooleanVar()
check_button_var.set(True)
only_play_check_button = Checkbutton(w, text="Only play", variable=check_button_var,
                                     onvalue=True, offvalue=False, height=1,
                                     width=20)
only_play_check_button.pack()

frame = Frame(w)
frame.pack()

# Final run button ********************
b = Button(
    frame,
    text='Run',
    bg="green",
    fg="white",
    padx="20",
    pady="5",
    command=run
)
b.pack(side=LEFT)

# Quit button *************************
quit_button = Button(
    frame,
    text='Quit',
    bg="red",
    fg="white",
    padx="20",
    pady="5",
    command=quit
)
quit_button.pack(side=RIGHT)

after_run_label = Label(w, text="")
after_run_label.pack()


mainloop()
