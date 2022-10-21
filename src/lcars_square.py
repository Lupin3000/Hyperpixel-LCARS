import tkinter as tk
import tkinter.font as tkf

from PIL import Image, ImageTk
from lcars.lcars_weather import OpenWeather
from lcars.lcars_system_metrics import HostMetrics, TimeMetrics
from lcars_base import LcarsBase


class LcarsSquare(LcarsBase):

    def __init__(self,
                 fullscreen: bool = False) -> None:
        super().__init__(title='LCARS SQUARE',
                         resolution='720x720+0+0',
                         fullscreen_mode=fullscreen,
                         verbose_mode=3)

        self.frame = None
        self.label_bg = None
        self.label_headline = None
        self.label_date = None
        self.label_host = None

    def _create_frames(self) -> None:
        background_color = '#000000'

        self.frame = tk.Frame(self.window, bg=background_color, height=720, width=720)
        self.frame.grid(column=0, row=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def _add_widgets(self) -> None:
        headline_color = '#FF7700'
        black_color = '#000000'
        blue_color = '#0080F4'

        img_bg = Image.open('./img/square.png')
        bg_bg = ImageTk.PhotoImage(img_bg)

        main_font = tkf.Font(family='Okuda', weight='normal', size=50)

        self.label_bg = tk.Label(self.frame, image=bg_bg, bg=black_color)
        self.label_bg.image = bg_bg
        self.label_bg.grid(column=0, row=0)

        self.label_headline = tk.Label(self.frame, font=main_font, bg=black_color, fg=headline_color,
                                       text='Raspberry LCARS')
        self.label_headline.place(anchor=tk.CENTER, relx=.8, rely=.1)

        self.label_date = tk.Label(self.frame, font=main_font, bg=blue_color, fg=black_color, text='')
        self.label_date.place(anchor=tk.CENTER, relx=.127, rely=.22)

        self.label_host = tk.Label(self.frame, font=main_font, bg=black_color, fg=blue_color, text='')
        self.label_host.place(anchor=tk.CENTER, relx=.85, rely=.45)

        self.window.after(10, self._update_widget)

    def _update_widget(self, update_after: int = 60000) -> None:
        super()._update_widget(update_after_milliseconds=int(update_after))

        weather_metrics = OpenWeather()
        print(weather_metrics.get_weather_metrics())

        self.label_date.config(text=TimeMetrics())
        self.label_host.config(text=HostMetrics())

        self.window.after(int(update_after), self._update_widget)


if __name__ == '__main__':
    LcarsSquare()
