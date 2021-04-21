# Final Sprint Project - Viro Labs Vaccine Tracker

# Authors: Evan Murphy, Stephen Menecola, Chris Osmond, Brad Rice

# Date: 04/12/2021

# ************* List of To-Do's ****************
# - Create Menu Bar (started)
# - Activate Save Function/Button (close to finished)
# - Validate Morning, Evening readings and Rate of Change (started)
# - Activate Linear Projection Function/Button (done)
# - Activate Add Data Function/Button (started)
# - Make Output box bigger (done)

# Set up tkinter, ttk, messagebox, datetime

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Set current date

current_date = datetime.datetime.now()

# Basic code for a window

window = Tk()
window.title("Viro Labs Vaccine Tracker")
window.geometry("700x400")

# Setting up the menu bar and options

menu_bar = Menu(window)
window.config(menu=menu_bar)

# Creating menu items

def our_command():
    pass

menu_file = Menu(menu_bar)
menu_bar.add_cascade(label='file', menu=menu_file)
menu_file.add_command(label='New...', command=our_command)

# Loading bacteria.dat file

def load_all_bacteria():

    file = open('Bacteria.dat', 'a')
    file.close()

    bacteria_defaults = ['Coccus', 'Bacillus', 'Spirillum', 'Rickettsia', 'Mycoplasma']

    file = open('Bacteria.dat', 'r')
    bacteria_list = file.readlines()
    file.close()

    if len(bacteria_list) < 5:
        with open('Bacteria.dat', 'w') as file:
            for item in bacteria_defaults:
                file.write('{}\n'.format(item))
                bacteria_list.append(item)
    return bacteria_list

bacteria_menu_list = load_all_bacteria()

# Loading medicine.dat file

def load_all_medicine():

    file = open('Medicine.dat', 'a')
    file.close()

    medicine_defaults = ['Control', 'Formula-FD102', 'Formula-FD201', 'Formula-FD202', 'Formula-FD505']

    file = open('Medicine.dat', 'r')
    medicine_list = file.readlines()
    file.close()

    if len(medicine_list) < 5:
        with open('Medicine.dat', 'w') as file:
            for item in medicine_defaults:
                file.write('{}\n'.format(item))
                medicine_list.append(item)
    return medicine_list

medicine_menu_list = load_all_medicine()

# Setting up frames

culture_information_frame = LabelFrame(window, text="Culture Information")
culture_information_frame.grid(row=0, column=0, padx=5, pady=5)

output_frame = LabelFrame(window, text="Output")
output_frame.grid(row=0, column=1, padx=5, pady=5, columnspan=5)

lb = Listbox(output_frame, width=30)
lb.grid(row=0, column=1)

confirm_button_frame = LabelFrame(window)
confirm_button_frame.grid(row=6, column=0, padx=5, pady=5)

button_frame = LabelFrame(window)
button_frame.grid(row=6, column=1, padx=5, pady=5)

# Setting up labels and entry boxes - Culture information frame

date = Label(culture_information_frame, text="Date")
date.grid(row=0, column=0)
date_sv = StringVar()
date_entry = Entry(culture_information_frame, textvariable=date_sv)
date_entry.grid(row=0, column=1)
date_entry.insert(END, current_date.strftime("%Y/%m/%d"))

culture_ID = Label(culture_information_frame, text="Culture ID")
culture_ID.grid(row=1, column=0)
culture_ID_sv = StringVar()
culture_ID_entry = Entry(culture_information_frame, textvariable=culture_ID_sv)
culture_ID_entry.grid(row=1, column=1)

bacteria_label = Label(culture_information_frame, text="Bacteria")
bacteria_label.grid(row=2, column=0, padx=5, pady=5)
bacteria_sv = StringVar(culture_information_frame)
bacteria_menu = OptionMenu(culture_information_frame, bacteria_sv, *bacteria_menu_list)
bacteria_menu.grid(row=2, column=1, padx=5, pady=5)

medicine_label = Label(culture_information_frame, text="Medicine")
medicine_label.grid(row=3, column=0, padx=5, pady=5)
medicine_sv = StringVar(culture_information_frame)
medicine_menu = OptionMenu(culture_information_frame, medicine_sv, *medicine_menu_list)
medicine_menu.grid(row=3, column=1, padx=5, pady=5)

first_reading = Label(culture_information_frame, text="First Reading (0hrs)")
first_reading.grid(row=4, column=0, padx=5, pady=5)
first_reading_sv = StringVar()
first_reading_entry = Entry(culture_information_frame, textvariable=first_reading_sv)
first_reading_entry.grid(row=4, column=1, padx=5, pady=5)

second_reading = Label(culture_information_frame, text="Second Reading (12hrs)")
second_reading.grid(row=5, column=0, padx=5, pady=5)
second_reading_sv = StringVar()
second_reading_entry = Entry(culture_information_frame, textvariable=second_reading_sv)
second_reading_entry.grid(row=5, column=1, padx=5, pady=5)

third_reading = Label(culture_information_frame, text="Third Reading (24hrs)")
third_reading.grid(row=6, column=0, padx=5, pady=5)
third_reading_sv = StringVar()
third_reading_entry = Entry(culture_information_frame, textvariable=third_reading_sv)
third_reading_entry.grid(row=6, column=1, padx=5, pady=5)

fourth_reading = Label(culture_information_frame, text="Fourth Reading (36hrs)")
fourth_reading.grid(row=7, column=0, padx=5, pady=5)
fourth_reading_sv = StringVar()
fourth_reading_entry = Entry(culture_information_frame, textvariable=fourth_reading_sv)
fourth_reading_entry.grid(row=7, column=1, padx=5, pady=5)

fifth_reading = Label(culture_information_frame, text="Fifth Reading (48hrs)")
fifth_reading.grid(row=8, column=0, padx=5, pady=5)
fifth_reading_sv = StringVar()
fifth_reading_entry = Entry(culture_information_frame, textvariable=fifth_reading_sv)
fifth_reading_entry.grid(row=8, column=1, padx=5, pady=5)

# Setting up buttons and their respective functions

def confirm_button_function():

    global get_date
    get_date = date_entry.get()
    return

    global get_culture_ID
    get_culture_ID = culture_ID_entry.get()
    return

    global get_bacteria
    get_bacteria = bacteria_sv.get()
    return

    global get_medicine
    get_medicine = medicine_sv.get()
    return

    global get_first
    try:
        get_first = int(first_reading_entry.get())
    except:
        messagebox.showerror("Input Error", "First entry field must be provided.")
        return

    global get_second
    try:
        get_second = int(second_reading_entry.get())
    except:
        messagebox.showerror("Input Error", "Second entry field must be provided.")
        return

    global get_third
    try:
        get_third = int(third_reading_entry.get())
    except:
        messagebox.showerror("Input Error", "Third entry field must be provided.")
        return

    global get_fourth
    try:
        get_fourth = int(fourth_reading_entry.get())
    except:
        messagebox.showerror("Input Error", "Fourth entry field must be provided.")
        return

    global get_fifth
    try:
        get_fifth = int(fifth_reading_entry.get())
    except:
        messagebox.showerror("Input Error", "Fifth entry field must be provided.")
        return

# Validating Culture Information Entries

    if get_date == "" or get_culture_ID == "" or get_bacteria == "" or get_medicine == "":
        messagebox.showerror("Input Error", "All culture information fields must be provided.")
        return

# Calculating rate of change

    global rate_of_change
    first_rate_of_change = ((get_second - get_first)-1)
    second_rate_of_change = ((get_third - get_second)-1)
    third_rate_of_change = ((get_fourth - get_third)-1)
    fourth_rate_of_change = ((get_fifth - get_fourth)-1)
    rate_of_change = (first_rate_of_change + second_rate_of_change + third_rate_of_change + fourth_rate_of_change)/4

# Displaying results to listbox

    lb.delete(0, END)
    lb.insert(END, "Date: {}".format(get_date))
    lb.insert(END, "Culture ID: {}".format(get_culture_ID))
    lb.insert(END, "Bacteria Type: {}".format(get_bacteria))
    lb.insert(END, "Medicine Type: {}".format(get_medicine))
    lb.insert(END, "First Population Reading: {}".format(get_first))
    lb.insert(END, "Second Population Reading: {}".format(get_second))
    lb.insert(END, "Third Population Reading: {}".format(get_third))
    lb.insert(END, "Fourth Population Reading: {}".format(get_fourth))
    lb.insert(END, "Fifth Population Reading: {}".format(get_fifth))
    lb.insert(END, "Calculated Rate of Change: {}".format(rate_of_change))


b1 = Button(culture_information_frame, text="Confirm", command=confirm_button_function)
b1.grid(row=9, column=1, padx=10, pady=10, sticky=N, columnspan=1)

def first_save_button_function():

# Create a simple dialog***

# Creating a Pop Up Window for the New Save File

    save_window = Toplevel()
    save_window.title('File Save')
    save_window.geometry('350x120')

# Save File Frame, Label + Entry Box

    save_frame = LabelFrame(save_window)
    save_frame.grid(row=0, column=0)
    save_file = Label(save_frame, text='Enter the name of the file you wish to save this data to \n'
                                        '(Entering a new file name will create a new file): ')
    save_file.grid(row=0, column=0, sticky='NESW')
    save_file_sv = StringVar()
    save_file_entry = Entry(save_frame, textvariable=save_file_sv)
    save_file_entry.grid(row=1, column=0, sticky='NESW')

# Getting the Entry Box Data

    global get_save_file
    get_save_file = save_file_entry.get()

    def second_save_button_function():

# Creating a File + Saving Data to it

        file_name = "{}.dat".format(get_save_file)
        file = open(file_name, 'a')
        file.write("{}\n".format(get_date))
        file.write("{}\n".format(get_culture_ID))
        file.write("{}\n".format(get_bacteria))
        file.write("{}\n".format(get_medicine))
        file.write("{}\n".format(get_first))
        file.write("{}\n".format(get_second))
        file.write("{}\n".format(rate_of_change))
        file.close()

    second_save_button_function()

# Setting up Second save button

    b6 = Button(save_window, text="Save", command=second_save_button_function)
    b6.grid(row=2, column=0)

# First save button

b2 = Button(button_frame, text="Save", command=first_save_button_function)
b2.grid(row=1, column=0, padx=10, pady=10, sticky=NW)

def linear_projection_button_function():

# Graphing equation =
# y = ax + b
# where b = (morning reading),
# a = ((evening reading) - (morning reading))/12

    x = np.linspace(-10,10,100)
    a = ((get_second) - (get_first))/12
    b = get_first
    y = a*x + b
    plt.plot(x, y, '-r', label='Rate of Change')
    plt.title('Graph of Rate of Change')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

# Linear Projection button

b3 = Button(button_frame, text="Linear Projection", command=linear_projection_button_function)
b3.grid(row=1, column=1, padx=10, pady=10, sticky=NE)

def add_data_button_function():

    new_bacteria = simpledialog.askstring("Add Bacteria", "What is your new Bacteria?")
    file = open('Bacteria.dat', 'a')
    file.write("{}\n".format(new_bacteria))
    file.close()

    new_medicine = simpledialog.askstring("Add Medicine", "What is your new Medicine?")
    file = open('Medicine.dat', 'a')
    file.write('{}'.format(new_medicine))
    file.close()

# Add data button

b4 = Button(button_frame, text="Add Data", command=add_data_button_function)
b4.grid(row=2, column=0, padx=10, pady=10, sticky=SW)

def exit_button_function():
    exit(0)

b5 = Button(button_frame, text="Exit", command=exit_button_function)
b5.grid(row=2, column=1, padx=10, pady=10, sticky=SE)

# Set up main loop

window.mainloop()