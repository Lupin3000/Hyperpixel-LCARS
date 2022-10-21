import tkinter as tk
import tkinter.font as tkf

from lcars_base import LcarsBase


class LcarsSquare(LcarsBase):

    def __init__(self,
                 fullscreen: bool = False) -> None:
        super().__init__(title='LCARS SQUARE',
                         resolution='720x720+0+0',
                         fullscreen=fullscreen)

        self.frame = None
        self.label_headline = None

    def _create_frames(self) -> None:
        background_color = '#000000'

        self.frame = tk.Frame(self.window, bg=background_color, height=50, width=720)
        self.frame.grid(column=0, row=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def _add_widgets(self) -> None:
        headline_color = '#FF7700'
        background_color = '#000000'

        main_font = tkf.Font(family='Okuda', weight='normal', size=50)

        self.label_headline = tk.Label(self.frame, font=main_font, bg=background_color, fg=headline_color, text='LCARS SQUARE')
        self.label_headline.place(anchor=tk.CENTER, relx=.5, rely=.5)


if __name__ == '__main__':
    LcarsSquare()
