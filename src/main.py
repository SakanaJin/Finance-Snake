import customtkinter as ctk
# from tkinter import Canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

BACKGROUND_COLOR_DARK = '#242424'

def button_action() -> None:
    print('Button Pressed')

def main() -> None:
    ctk.set_appearance_mode('dark')
    # ctk.set_appearance_mode('light')
    # ctk.set_default_color_theme('green')
    ctk.set_default_color_theme('blue')
    # ctk.set_default_color_theme('dark-blue')
    root = ctk.CTk()
    root.geometry("500x350")
    root.title('Finance Snake')
    root.wm_iconbitmap("./favicon.ico")
    root.grid_columnconfigure(0, weight=1)
    button = ctk.CTkButton(root, text='Test', command=button_action)
    button.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    y = np.array([35,25,25,15])
    fig1, ax = plt.subplots()
    fig1.set_facecolor(BACKGROUND_COLOR_DARK)
    ax.pie(y)

    canvas = FigureCanvasTkAgg(figure=fig1, master=root)
    widget = canvas.get_tk_widget()
    widget.grid(row=1, column=0, padx=20, pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()