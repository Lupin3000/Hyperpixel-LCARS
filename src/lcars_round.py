import tkinter as tk
from typing import Literal

from src.lcars.lcars_app_ui import LcarsUi


class LcarsRound(LcarsUi):

    def __init__(self, fullscreen: bool = False, verbose: Literal[1, 2, 3] = 3) -> None:
        super().__init__(w_width=480, w_height=480, w_title='ROUND', w_fullscreen=fullscreen, w_verbose=verbose)

    def _add_widgets(self) -> None:
        self._set_fonts(headline=40, paragraph=25, sidebar=25)
        self._set_colors(headline='#FF7700', blue='#0080F4')
        self._set_background(image_path='./img/round.png')

        # top
        self.label_temperature = tk.Label(self.frames, font=self.fonts['paragraph'], fg=self.colors['blue'],
                                          bg=self.colors['black'])
        self.label_temperature.place(anchor=tk.CENTER, relx=.35, rely=.4)

        self.label_pressure = tk.Label(self.frames, font=self.fonts['paragraph'], fg=self.colors['blue'],
                                       bg=self.colors['black'])
        self.label_pressure.place(anchor=tk.CENTER, relx=.5, rely=.4)

        self.label_humidity = tk.Label(self.frames, font=self.fonts['paragraph'], fg=self.colors['blue'],
                                       bg=self.colors['black'])
        self.label_humidity.place(anchor=tk.CENTER, relx=.65, rely=.4)

        self.label_wind = tk.Label(self.frames, font=self.fonts['paragraph'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_wind.place(anchor=tk.CENTER, relx=.8, rely=.4)

        self.label_os = tk.Label(self.frames, font=self.fonts['headline'], fg=self.colors['headline'],
                                 bg=self.colors['black'])
        self.label_os.place(anchor=tk.CENTER, relx=.85, rely=.1)

        # side bar
        self.label_ram = tk.Label(self.frames, font=self.fonts['side_bar'], fg=self.colors['black'],
                                  bg=self.colors['red'])
        self.label_ram.place(anchor=tk.CENTER, relx=.185, rely=.6)

        self.label_date = tk.Label(self.frames, font=self.fonts['side_bar'], fg=self.colors['black'],
                                   bg=self.colors['blue'])
        self.label_date.place(anchor=tk.CENTER, relx=.185, rely=.72)

        # bottom
        self.label_host = tk.Label(self.frames, font=self.fonts['headline'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_host.place(anchor=tk.CENTER, relx=.45, rely=.275)

        # reload
        self.window.after(10, self._update_widget)


if __name__ == '__main__':
    LcarsRound(fullscreen=False, verbose=3)
