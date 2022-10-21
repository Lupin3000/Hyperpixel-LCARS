import tkinter as tk
import tkinter.font as tkf
from typing import Literal

from PIL import Image, ImageTk

from src.lcars.lcars_app_ui import LcarsUi


class LcarsRound(LcarsUi):

    def __init__(self, fullscreen: bool = False, verbose: Literal[1, 2, 3] = 3) -> None:
        super().__init__(w_width=480, w_height=480, w_title='ROUND', w_fullscreen=fullscreen, w_verbose=verbose)

        self.label_bg = None
        self.label_headline = None

    def _add_widgets(self) -> None:
        headline_color = '#FF7700'
        black_color = '#000000'
        blue_color = '#7788FF'

        main_font = tkf.Font(family='Okuda', weight='normal', size=50)

        self.label_headline = tk.Label(self.frame, font=main_font, bg=black_color, fg=headline_color, text='LCARS ROUND')
        self.label_headline.place(anchor=tk.CENTER, relx=.775, rely=.1)

        self.label_date = tk.Label(self.frame, font=main_font, bg=blue_color, fg=black_color, text='')
        self.label_date.place(anchor=tk.CENTER, relx=.5, rely=.7)

        self.label_host = tk.Label(self.frame, font=main_font, bg=black_color, fg=blue_color, text='')
        self.label_host.place(anchor=tk.CENTER, relx=.85, rely=.45)

        self.window.after(10, self._update_widget)


if __name__ == '__main__':
    LcarsRound(fullscreen=False, verbose=3)
