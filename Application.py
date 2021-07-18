import tkinter
from tkinter import *
from scraper import *
from tkcalendar import Calendar
#  from PIL import ImageTk, Image


SHIFT_OPTIONS = [
    'VTO',
    'VET'
]

TIME_OPTIONS = [
    '03:00',
    '09:00',
    '14:30',
    '20:00',
    '22:30'
]


def startSelenium():
    startScraper(get_shift_type(), get_time_choice(), get_cal())


def get_shift_type():
    return shift_type


def get_time_choice():
    return time_choice


def get_cal():
    return cal.get_date()


# SHIFT OPTIONS MENU
root = Tk()
root.title('Amazon Time Skimmer')
root.geometry("400x400")

shift_type = StringVar()
shift_type.set(SHIFT_OPTIONS[0])  # default value

st = OptionMenu(root, shift_type, *SHIFT_OPTIONS)
st.pack()

# TIME OPTIONS MENU
time_choice = StringVar()
time_choice.set(TIME_OPTIONS[0])

tc = tkinter.OptionMenu(root, time_choice, *TIME_OPTIONS)
tc.pack()

# DATE OPTION
cal = Calendar(root, selectmode='day', year=2021, month=7, day=12)
cal.pack()
# SUBMIT BUTTON
submitButton = Button(root, text="Submit", command=startSelenium)
submitButton.pack()

root.mainloop()
