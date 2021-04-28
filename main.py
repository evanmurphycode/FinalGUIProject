# Final Sprint Project - Viro Labs Vaccine Tracker

# Authors: Evan Murphy, Stephen Menecola, Chris Osmond, Brad Rice

# Date: 04/12/2021

# ************* List of To-Do's ****************
# - Create Menu Bar (not done)
# - Activate Save Function/Button (done)
# - Validate Morning, Evening readings and Rate of Change (done)
# - Activate Linear Projection Function/Button (done)
# - Validate Save, Linear Projection, & Add Data Buttons?! (not done)
# - Activate Add Data Function/Button (done)
# - Format Output box bigger (done)
# - Make it look pretty (not done)

# Set up tkinter, ttk, messagebox, datetime

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as font
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Set current date

current_date = datetime.datetime.now()

# Basic code for a window

window = Tk()
window.title("Viro Labs Vaccine Tracker")
window.geometry("710x520")
#window.resizable(0, 0)
window.config(bg="#e9ecef")
# Loading Bacteria.dat file

def load_all_bacteria():

    file = open('Bacteria.dat', 'a')
    file.close()

    bacteria_defaults = ['Coccus', 'Bacillus', 'Spirillum', 'Rickettsia', 'Mycoplasma']

    file = open('Bacteria.dat', 'r')
    bacteria_list = file.readlines()
    file.close()

    # If Bacteria.dat didn't exist before launching program, load default values
    if len(bacteria_list) < 5:
        with open('Bacteria.dat', 'w') as file:
            for item in bacteria_defaults:
                file.write('{}\n'.format(item))
                bacteria_list.append(item)
    return bacteria_list

bacteria_menu_list = load_all_bacteria()

# Loading Medicine.dat file

def load_all_medicine():

    file = open('Medicine.dat', 'a')
    file.close()

    medicine_defaults = ['Control', 'Formula-FD102', 'Formula-FD201', 'Formula-FD202', 'Formula-FD505']

    file = open('Medicine.dat', 'r')
    medicine_list = file.readlines()
    file.close()

    # If Medicine.dat didn't exist before launching program, load default values
    if len(medicine_list) < 5:
        with open('Medicine.dat', 'w') as file:
            for item in medicine_defaults:
                file.write('{}\n'.format(item))
                medicine_list.append(item)
    return medicine_list

medicine_menu_list = load_all_medicine()

# Setting up frames

culture_information_frame = LabelFrame(window, text="Culture Information")
culture_information_frame.grid(row=0, column=0, columnspan=2, padx=16, pady=8)

culture_readings_frame = LabelFrame(window, text="Culture Readings")
culture_readings_frame.grid(row=0, column=1, padx=5, pady=5, sticky=N)

output_frame = LabelFrame(window, text="Output Window")
output_frame.grid(row=2, column=0, padx=8, pady=8, sticky=W)

lb = Listbox(output_frame, width=37)
lb.grid(row=2, column=0, columnspan=1, padx=8, pady=8, sticky="NW")

button_frame = LabelFrame(window)
button_frame.grid(row=2, column=2, padx=16, pady=16, columnspan=2, sticky=NW)

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

morning_reading = Label(culture_readings_frame, text="Morning Reading (6am)")
morning_reading.grid(row=0, column=0, padx=5, pady=5)
morning_reading_sv = StringVar()
morning_reading_entry = Entry(culture_readings_frame, textvariable=morning_reading_sv)
morning_reading_entry.grid(row=0, column=1, padx=5, pady=5)

evening_reading = Label(culture_readings_frame, text="Evening Reading (6pm)")
evening_reading.grid(row=1, column=0, padx=5, pady=5)
evening_reading_sv = StringVar()
evening_reading_entry = Entry(culture_readings_frame, textvariable=evening_reading_sv)
evening_reading_entry.grid(row=1, column=1, padx=5, pady=5)

# Setting up buttons and their respective functions

def confirm_button_function():

    global get_date
    get_date = date_sv.get()

    global get_culture_ID
    get_culture_ID = culture_ID_sv.get()

    global get_bacteria
    get_bacteria = bacteria_sv.get()

    global get_medicine
    get_medicine = medicine_sv.get()

    global get_morning
    try:
        get_morning = int(morning_reading_entry.get())
    except:
        messagebox.showerror("Input Error", "Morning entry field must be provided.")
        return

    global get_evening
    try:
        get_evening = int(evening_reading_entry.get())
    except:
        messagebox.showerror("Input Error", "Evening entry field must be provided.")
        return

# Validating Culture Information Entries

    if get_date == "" or get_culture_ID == "" or get_bacteria == "" or get_medicine == "":
        messagebox.showerror("Input Error", "All culture information fields must be provided.")
        return

# Calculating rate of change

    global rate_of_change
    rate_of_change = ((get_evening - get_morning)-1)

# Displaying results to listbox

    lb.delete(0, END)
    lb.insert(END, "{}".format(get_date))
    lb.insert(END, "{}".format(get_culture_ID))
    lb.insert(END, "{}".format(get_bacteria))
    lb.insert(END, "{}".format(get_medicine))
    lb.insert(END, "{}".format(get_morning))
    lb.insert(END, "{}".format(get_evening))
    lb.insert(END, "{}".format(rate_of_change))


b1 = Button(culture_readings_frame, text="Confirm", command=confirm_button_function)
b1.grid(row=5, column=1, padx=10, pady=10, sticky=NSEW, columnspan=1)

def save_button_function():

    save_file = simpledialog.askstring("Save Data", "What would you like to name your file?")
    file_name = "{}.dat".format(save_file)
    file = open(file_name, 'a')
    file.write("{}\n".format(get_date))
    file.write("{}\n".format(get_culture_ID))
    file.write("{}\n".format(get_bacteria))
    file.write("{}\n".format(get_medicine))
    file.write("{}\n".format(get_morning))
    file.write("{}\n".format(get_evening))
    file.write("{}\n".format(rate_of_change))
    file.close()

# Setting up save button

b2 = Button(button_frame, text="Save", command=save_button_function)
b2.grid(row=1, column=0, padx=10, pady=10, sticky=NW)

def linear_projection_button_function():

    c = simpledialog.askinteger("1st X Value", "What is your first x value?")
    d = simpledialog.askinteger("2nd X Value", "What is your second x value?")
    x = np.linspace(c,d,100)
    a = ((get_evening) - (get_morning))/12
    b = get_morning
    y = a*x + b
    plt.plot(x, y, '-Dm', label='Rate of Change')
    plt.title('Linear Projection')
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
    file.write('{}\n'.format(new_medicine))
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