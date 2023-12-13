import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

root = Tk()
root.title()  # need to specify title
root.iconbitmap()  # need to specify the icon
root.geometry("500x500")

# Defining the font
my_font = Font(
    family="Bradley Hand",
    size=30,
    weight="bold"
)

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Listbox
my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

# Creating a Fake List
#stuff = ["Watch Netflix", "Buy Groceries", "Take a nap", "Wash the Dishes"]
# Adding Fake List to the listbox
#for item in stuff:
#    my_list.insert(END, item)

# Creating scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Adding a scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Creating an Entry Box to add items to the list
my_entry = Entry(root, font=("Helvetica", 24), width=24)
my_entry.pack(pady=20)

# Creating a Button Frame
button_frame = Frame(root)
button_frame.pack(pady=20)


# FUNCTIONS


def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_off_item():
    # Cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    # Get Rid of selection Bar
    my_list.selection_clear(0, END)


def uncross_item():
    # Uncross item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    # Get Rid of selection Bar
    my_list.selection_clear(0, END)


def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))

        else:
            count += 1


def save_list():
    file_name = filedialog.asksaveasfilename(
        intialdir="/Users/jyotishkade/Desktop",  # Mention your directory where you want to save the file
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        # Delete Crossed off items
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))

            else:
                count += 1
        # Get all the things from the list
        stuff = my_list.get(0, END)

        # open the file
        output_file = open(file_name, 'wb')

        # actually add the stuff to the file
        pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(
        intialdir="/Users/jyotishkade/Desktop",  # Mention your directory where you want to save the file
        title="Open File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        # Delete currently open list
        my_list.delete(0, END)

        # open the file
        input_file = open(file_name, 'rb')

        # Load the data from the file
        stuff = pickle.load(input_file)

        # output stuff to the screen
        for item in stuff:
            my_list.insert(END, item)


def clear_list():
    my_list.delete(0, END)


#  Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#  Adding items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Adding dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)

# Adding some buttons


delete_button = Button(button_frame, text="Delete item", command=delete_item)
add_button = Button(button_frame, text="Add item", command=add_item)
cross_off_button = Button(button_frame, text="Cross off item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross item", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()
