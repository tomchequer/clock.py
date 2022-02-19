#this will be a simple clock app with maybe a timer ? i dont know yet

#built with tk and without OOP 


from tkinter import *
import time
import math


#constants
FONT_NAME = 'Courier'


#functions

def display_time(value: int):  
    
    stringed_time = time.strftime('%H: %M: %S')

    time_label.config(text=stringed_time)
    time_label.after(1000, display_time)


def get_timezone_input(timezone):
    string = variable.get()
    number = int(string[:-4])
    return number



def change_mode():
    pass

#creating a window


window = Tk()

window.title('clock widget')
window.maxsize(height=500,width=450)
window.config(padx=10, pady=5, bg='#f89c2c')
window.resizable(width=False, height=False)


#creating a canvas 

canvas = Canvas(width=350, height=350, background='#f89c2c', highlightthickness=0)
clock_png = PhotoImage(file='clock.png')
image_setup = canvas.create_image(200, 200, anchor="center", image = clock_png)

canvas.grid(row=2, column=3)



#-- labels --#

time_label = Label(text='0',background='#f05454',font=(FONT_NAME, 20, "bold"))
time_label.grid(row=2, column=3, rowspan=5)

# button #

mode = Button(text='mode', command=change_mode)
mode.grid(row=3,column=3, pady=5)

#menu
variable = StringVar(window)
variable.set("timezone") # default value


timezone_list = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
full_list = [str(i) + ' GMT' for i in timezone_list]
timezone = OptionMenu(window, variable, *full_list, command=change_timezone)
timezone.grid(row=4,column=3)


display_time(-3)
window.mainloop()
   
   
    