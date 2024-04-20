#version 0.2
DEBUG = 0
import tkinter as tk
import re, os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window = tk.Tk()
window.title("Dark and Darker Gear Score")
def show_coordinates(event):
    """
    Display the current coordinates of the mouse cursor.
    """
    x, y = event.x, event.y
    coordinates_label.config(text=f"X: {x}, Y: {y}")

def get_selected_values(*args):
    score = \
    int(weapon1_L_value.get().split(' ')[1]) + \
    int(weapon1_R_value.get().split(' ')[1]) + \
    int(weapon1_LR_value.get().split(' ')[1]) + \
    int(weapon2_L_value.get().split(' ')[1]) + \
    int(weapon2_R_value.get().split(' ')[1]) + \
    int(weapon2_LR_value.get().split(' ')[1]) + \
    int(head_value.get().split(' ')[1]) + \
    int(hands_value.get().split(' ')[1]) + \
    int(foot_value.get().split(' ')[1]) + \
    int(chest_value.get().split(' ')[1]) + \
    int(legs_value.get().split(' ')[1]) + \
    int(back_value.get().split(' ')[1]) + \
    int(necklace_value.get().split(' ')[1]) + \
    int(ring_L_value.get().split(' ')[1]) + \
    int(ring_R_value.get().split(' ')[1]) + \
    get_int(ut_junk.get())*2 + \
    get_int(ut_poor.get())*3 + \
    get_int(ut_common.get())*4 + \
    get_int(ut_uncommon.get())*6 + \
    get_int(ut_rare.get())*8 + \
    get_int(ut_epic.get())*12 + \
    get_int(ut_legendary.get())*16 + \
    get_int(ut_unique.get())*20 
    coordinates_label.config(text=("Gear Score = "+str(score)))
    
def get_int(input_string):
    # Use regular expression to find all digits in the string
    digits = re.findall(r'\d', input_string)
    
    # Join the digits together into a single string
    digits_str = ''.join(digits)
    
    # Convert the string of digits into an integer
    if len(digits_str)>0:
        result = int(digits_str)
    else:
        result = 0
    
    return result

# Load the image
background_image_path = resource_path("background.png")
background_image = tk.PhotoImage(file=background_image_path)

# Get the dimensions of the image
width = background_image.width()
height = background_image.height()

# Set the window size to match the image dimensions
window.geometry(f"{width}x{height}")

# Create a label with the image
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0)

# Create a label to display coordinates
coordinates_label = tk.Label(window, text="Gear Score = 0")
coordinates_label.pack()

# Bind the mouse motion event to the show_coordinates function
if DEBUG == True:
    window.bind("<Motion>", show_coordinates)


# Define the options and their respective colors
main_hand_weapon_options = ["Main-Hand 0", "Junk 9", "Poor 13","Common 18","Uncommon 27","Rare 36","Epic 54","Legendary 72","Unique 125"]
off_hand_weapon_options = ["Off-Hand 0", "Junk 7", "Poor 10","Common 14","Uncommon 21","Rare 28","Epic 42","Legendary 56","Unique 100"]
two_hand_weapon_options = ["Two-Hand 0", "Junk 15", "Poor 22","Common 30","Uncommon 45","Rare 60","Epic 90","Legendary 120","Unique 175"]
head_options = ["None 0", "Junk 4", "Poor 6","Common 8","Uncommon 12","Rare 16","Epic 24","Legendary 32","Unique 40"]
chest_options = ["None 0", "Junk 5", "Poor 7","Common 10","Uncommon 15","Rare 20","Epic 30","Legendary 40","Unique 50"]
accessory_options = ["None 0", "Uncommon 9","Rare 12","Epic 18","Legendary 24","Unique 30"]
# Create StringVar to store the selected option
weapon1_L_value = tk.StringVar()
weapon1_R_value = tk.StringVar()
weapon1_LR_value = tk.StringVar()

weapon2_L_value = tk.StringVar()
weapon2_R_value = tk.StringVar()
weapon2_LR_value = tk.StringVar()

head_value = tk.StringVar()
hands_value = tk.StringVar()
foot_value = tk.StringVar()

chest_value = tk.StringVar()
legs_value = tk.StringVar()
back_value = tk.StringVar()

necklace_value = tk.StringVar()
ring_L_value = tk.StringVar()
ring_R_value = tk.StringVar()


# Set the initial selected option
weapon1_L_value.set(main_hand_weapon_options[0])
weapon1_R_value.set(off_hand_weapon_options[0])
weapon1_LR_value.set(two_hand_weapon_options[0])

weapon2_L_value.set(main_hand_weapon_options[0])
weapon2_R_value.set(off_hand_weapon_options[0])
weapon2_LR_value.set(two_hand_weapon_options[0])

head_value.set(head_options[0])
hands_value.set(head_options[0])
foot_value.set(head_options[0])

chest_value.set(chest_options[0])
legs_value.set(chest_options[0])
back_value.set(chest_options[0])

necklace_value.set(accessory_options[0])
ring_L_value.set(accessory_options[0])
ring_R_value.set(accessory_options[0])


# Create the OptionMenu with the defined options and colors
weapon1_L = tk.OptionMenu(window, weapon1_L_value, *main_hand_weapon_options)
weapon1_L.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
weapon1_L.place(x=0, y=128)  # Place the dropdown menu at the specified location

weapon1_R = tk.OptionMenu(window, weapon1_R_value, *off_hand_weapon_options)
weapon1_R.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
weapon1_R.place(x=120, y=128)  # Place the dropdown menu at the specified location

weapon1_LR = tk.OptionMenu(window, weapon1_LR_value, *two_hand_weapon_options)
weapon1_LR.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
weapon1_LR.place(x=60, y=90)  # Place the dropdown menu at the specified location

weapon2_L = tk.OptionMenu(window, weapon2_L_value, *main_hand_weapon_options)
weapon2_L.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
weapon2_L.place(x=470, y=128)  # Place the dropdown menu at the specified location

weapon2_R = tk.OptionMenu(window, weapon2_R_value, *off_hand_weapon_options)
weapon2_R.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
weapon2_R.place(x=590, y=128)  # Place the dropdown menu at the specified location

weapon2_LR = tk.OptionMenu(window, weapon2_LR_value, *two_hand_weapon_options)
weapon2_LR.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
weapon2_LR.place(x=530, y=90)  # Place the dropdown menu at the specified location

head = tk.OptionMenu(window, head_value, *head_options)
head.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
head.place(x=275, y=50)  # Place the dropdown menu at the specified location

hands = tk.OptionMenu(window, hands_value, *head_options)
hands.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
hands.place(x=155, y=285)  # Place the dropdown menu at the specified location

foot = tk.OptionMenu(window, foot_value, *head_options)
foot.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
foot.place(x=430, y=470)  # Place the dropdown menu at the specified location

chest = tk.OptionMenu(window, chest_value, *chest_options)
chest.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
chest.place(x=275, y=230)  # Place the dropdown menu at the specified location

legs = tk.OptionMenu(window, legs_value, *chest_options)
legs.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
legs.place(x=275, y=435)  # Place the dropdown menu at the specified location

back = tk.OptionMenu(window, back_value, *chest_options)
back.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
back.place(x=425, y=275)  # Place the dropdown menu at the specified location

necklace = tk.OptionMenu(window, necklace_value, *accessory_options)
necklace.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
necklace.place(x=375, y=95)  # Place the dropdown menu at the specified location

ring_L = tk.OptionMenu(window, ring_L_value, *accessory_options)
ring_L.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
ring_L.place(x=175, y=360)  # Place the dropdown menu at the specified location

ring_R = tk.OptionMenu(window, ring_R_value, *accessory_options)
ring_R.config(bg="white", fg="black")  # Set background and text color of the dropdown menu
ring_R.place(x=420, y=360)  # Place the dropdown menu at the specified location


ut_junk = tk.Entry(width=5)
ut_poor = tk.Entry(width=5)
ut_common = tk.Entry(width=5)
ut_uncommon = tk.Entry(width=5)
ut_rare = tk.Entry(width=5)
ut_epic = tk.Entry(width=5)
ut_legendary = tk.Entry(width=5)
ut_unique = tk.Entry(width=5)

ut_junk.place(x=107, y=407)
ut_poor.place(x=107, y=433)
ut_common.place(x=107, y=460)
ut_uncommon.place(x=107, y=487)
ut_rare.place(x=107, y=512)
ut_epic.place(x=107, y=537)
ut_legendary.place(x=107, y=562)
ut_unique.place(x=107, y=587)


# Bind the get_selected_values function to variable updates
weapon1_L_value.trace_add("write", get_selected_values)
weapon1_R_value.trace_add("write", get_selected_values)
weapon1_LR_value.trace_add("write", get_selected_values)

weapon2_L_value.trace_add("write", get_selected_values)
weapon2_R_value.trace_add("write", get_selected_values)
weapon2_LR_value.trace_add("write", get_selected_values)

head_value.trace_add("write", get_selected_values)
hands_value.trace_add("write", get_selected_values)
foot_value.trace_add("write", get_selected_values)

chest_value.trace_add("write", get_selected_values)
legs_value.trace_add("write", get_selected_values)
back_value.trace_add("write", get_selected_values)

necklace_value.trace_add("write", get_selected_values)
ring_L_value.trace_add("write", get_selected_values)
ring_R_value.trace_add("write", get_selected_values)

ut_junk.bind("<KeyRelease>", get_selected_values)
ut_poor.bind("<KeyRelease>", get_selected_values)
ut_common.bind("<KeyRelease>", get_selected_values)
ut_uncommon.bind("<KeyRelease>", get_selected_values)
ut_rare.bind("<KeyRelease>", get_selected_values)
ut_epic.bind("<KeyRelease>", get_selected_values)
ut_legendary.bind("<KeyRelease>", get_selected_values)
ut_unique.bind("<KeyRelease>", get_selected_values)

window.mainloop()
