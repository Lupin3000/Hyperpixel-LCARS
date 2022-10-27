import os
import tkinter as tk

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from lcars.lcars_app_ui import LcarsUi


class LcarsRound(LcarsUi):

    def __init__(self, fullscreen: bool = False, verbose: Literal[1, 2, 3] = 3) -> None:
        super().__init__(w_width=480, w_height=480, w_title='ROUND', w_fullscreen=fullscreen, w_verbose=verbose)

    def _add_widgets(self) -> None:
        self._set_fonts(headline=40, paragraph_top=32, time=125, paragraph_bottom=25, sidebar=25)
        self._set_colors(headline='#FF7700', blue='#0080F4')

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'img/round.png')
        self._set_background(image_path=filename)

        # top
        self.label_temperature = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                          bg=self.colors['black'])
        self.label_temperature.place(anchor=tk.CENTER, relx=.4, rely=.3)

        self.label_pressure = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                       bg=self.colors['black'])
        self.label_pressure.place(anchor=tk.CENTER, relx=.6, rely=.3)

        self.label_humidity = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                       bg=self.colors['black'])
        self.label_humidity.place(anchor=tk.CENTER, relx=.4, rely=.4)

        self.label_wind = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_wind.place(anchor=tk.CENTER, relx=.6, rely=.4)

        self.label_os = tk.Label(self.frames[0], font=self.fonts['headline'], fg=self.colors['headline'],
                                 bg=self.colors['black'])
        self.label_os.place(anchor=tk.CENTER, relx=.8, rely=.39)

        self.label_date = tk.Label(self.frames[0], font=self.fonts['paragraph_bottom'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_date.place(anchor=tk.CENTER, relx=.8, rely=.625)

        self.label_ram = tk.Label(self.frames[0], font=self.fonts['paragraph_bottom'], fg=self.colors['blue'],
                                  bg=self.colors['black'])
        self.label_ram.place(anchor=tk.CENTER, relx=.8, rely=.7)

        # bottom
        self.label_time = tk.Label(self.frames[0], font=self.fonts['time'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_time.place(anchor=tk.CENTER, relx=.5, rely=.625)

        self.label_host = tk.Label(self.frames[0], font=self.fonts['paragraph_bottom'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_host.place(anchor=tk.CENTER, relx=.3, rely=.865)

        # reload
        self.window.after(10, self._update_widget)


if __name__ == '__main__':
    LcarsRound(fullscreen=False, verbose=2)
