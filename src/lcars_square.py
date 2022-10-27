import os
import tkinter as tk

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from lcars.lcars_app_ui import LcarsUi


class LcarsSquare(LcarsUi):

    def __init__(self, fullscreen: bool = False, verbose: Literal[1, 2, 3] = 3) -> None:
        super().__init__(w_width=720, w_height=720, w_title='SQUARE', w_fullscreen=fullscreen, w_verbose=verbose)

    def _add_widgets(self) -> None:
        self._set_fonts(headline=50, paragraph_top=50, time=200, paragraph_bottom=30, sidebar=25)
        self._set_colors(headline='#FF7700', blue='#0080F4')

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'img/square.png')
        self._set_background(image_path=filename)

        # top
        label_txt_outside = tk.Label(self.frames[0], font=self.fonts['headline'], text='Outside',
                                     fg=self.colors['headline'], bg=self.colors['black'])
        label_txt_outside.place(anchor=tk.CENTER, relx=.9, rely=.05)

        self.label_temperature = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                          bg=self.colors['black'])
        self.label_temperature.place(anchor=tk.CENTER, relx=.45, rely=.15)

        self.label_pressure = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                       bg=self.colors['black'])
        self.label_pressure.place(anchor=tk.CENTER, relx=.45, rely=.25)

        self.label_humidity = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                       bg=self.colors['black'])
        self.label_humidity.place(anchor=tk.CENTER, relx=.8, rely=.25)

        self.label_wind = tk.Label(self.frames[0], font=self.fonts['paragraph_top'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_wind.place(anchor=tk.CENTER, relx=.8, rely=.15)

        # bottom
        self.label_os = tk.Label(self.frames[0], font=self.fonts['headline'], fg=self.colors['headline'],
                                 bg=self.colors['black'])
        self.label_os.place(anchor=tk.CENTER, relx=.9, rely=.5)

        self.label_host = tk.Label(self.frames[0], font=self.fonts['paragraph_bottom'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_host.place(anchor=tk.CENTER, relx=.4, rely=.9)

        self.label_time = tk.Label(self.frames[0], font=self.fonts['time'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_time.place(anchor=tk.CENTER, relx=.6, rely=.65)

        self.label_date = tk.Label(self.frames[0], font=self.fonts['paragraph_bottom'], fg=self.colors['blue'],
                                   bg=self.colors['black'])
        self.label_date.place(anchor=tk.CENTER, relx=.6, rely=.9)

        self.label_ram = tk.Label(self.frames[0], font=self.fonts['paragraph_bottom'], fg=self.colors['blue'],
                                  bg=self.colors['black'])
        self.label_ram.place(anchor=tk.CENTER, relx=.8, rely=.9)

        # reload
        self.window.after(10, self._update_widget)


if __name__ == '__main__':
    LcarsSquare(fullscreen=False, verbose=3)
