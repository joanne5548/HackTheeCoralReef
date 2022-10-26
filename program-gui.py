from tkinter import *

window = Tk()
window.title('My First Hackathon')
window.geometry('1200x900')

# World Map Placement
world_map = PhotoImage(file='world-map.png')
map_label = Label(window, image=world_map, bg='#8bbbe8')
map_label.place(relx=0.5, rely=0.5, anchor='center')

# Title
title_label = Label(window, text='Coral Reef Simulator')
title_label.place(relx=0.5, rely=0, anchor='n')

window.mainloop()
