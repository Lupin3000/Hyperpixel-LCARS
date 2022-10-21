import tkinter as tk
import tkinter.font as tkf
from typing import Literal

from PIL import Image, ImageTk

from src.lcars.lcars_app_ui import LcarsUi


class LcarsRectangle(LcarsUi):

    def __init__(self, fullscreen: bool = False, verbose: Literal[1, 2, 3] = 3) -> None:
        super().__init__(w_width=800, w_height=480, w_title='RECTANGLE', w_fullscreen=fullscreen, w_verbose=verbose)

        self.label_bg = None
        self.label_headline = None

    def _add_widgets(self) -> None:
        img_bg = Image.open('./img/rectangle.png')
        bg_bg = ImageTk.PhotoImage(img_bg)

        headline_color = '#FF7700'
        black_color = '#000000'
        blue_color = '#7788FF'

        main_font = tkf.Font(family='Okuda', weight='normal', size=50)

        self.label_bg = tk.Label(self.frame, image=bg_bg, bg=black_color)
        self.label_bg.image = bg_bg
        self.label_bg.grid(column=0, row=0)

        self.label_headline = tk.Label(self.frame, font=main_font, bg=black_color, fg=headline_color,
                                       text='Raspberry RECTANGLE')
        self.label_headline.place(anchor=tk.CENTER, relx=.8, rely=.1)

        self.label_date = tk.Label(self.frame, font=main_font, bg=blue_color, fg=black_color, text='')
        self.label_date.place(anchor=tk.CENTER, relx=.075, rely=.2)

        self.label_host = tk.Label(self.frame, font=main_font, bg=black_color, fg=blue_color, text='')
        self.label_host.place(anchor=tk.CENTER, relx=.85, rely=.45)

        self.window.after(10, self._update_widget)


if __name__ == '__main__':
    LcarsRectangle(fullscreen=False, verbose=3)
