import time
import tkinter as tk
import tkinter.font as tkf

from lcars_base import LcarsBase


class LcarsRectangle(LcarsBase):

    def __init__(self,
                 fullscreen: bool = False) -> None:
        super().__init__(title='LCARS RECTANGLE',
                         resolution='800x480+0+0',
                         fullscreen_mode=fullscreen,
                         verbose_mode=3)

        self.frame = None
        self.label_headline = None
        self.label_date = None

    def _create_frames(self) -> None:
        background_color = '#000000'

        self.frame = tk.Frame(self.window, bg=background_color, height=480, width=800)
        self.frame.grid(column=0, row=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def _add_widgets(self) -> None:
        headline_color = '#FF7700'
        black_color = '#000000'
        blue_color = '#7788FF'

        main_font = tkf.Font(family='Okuda', weight='normal', size=50)

        self.label_headline = tk.Label(self.frame, font=main_font, bg=black_color, fg=headline_color, text='LCARS RECTANGLE')
        self.label_headline.place(anchor=tk.CENTER, relx=.825, rely=.1)

        self.label_date = tk.Label(self.frame, font=main_font, bg=blue_color, fg=black_color, text='')
        self.label_date.place(anchor=tk.CENTER, relx=.5, rely=.7)

        self.window.after(10, self._update_widget)

    def _update_widget(self, update_after: int = 60000) -> None:
        super()._update_widget(update_after_milliseconds=int(update_after))

        current_date = f"{time.strftime('%d')}-{time.strftime('%m')}{time.strftime('%Y')}"

        self.label_date.config(text=current_date)

        self.window.after(int(update_after), self._update_widget)


if __name__ == '__main__':
    LcarsRectangle()
