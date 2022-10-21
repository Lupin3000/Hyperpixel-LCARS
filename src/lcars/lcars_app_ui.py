import tkinter as tk

from src.lcars.lcars_app_base import LcarsBase
from src.lcars.lcars_system_metrics import HostMetrics, TimeMetrics
from src.lcars.lcars_weather import OpenWeather


class LcarsUi(LcarsBase):

    def __init__(self, w_width: int, w_height: int, w_title: str, w_verbose: int, w_fullscreen: bool = False) -> None:
        self.frame = None
        self.frame_width = int(w_width)
        self.frame_height = int(w_height)

        self.label_date = None
        self.label_host = None

        super().__init__(app_title=f"LCARS {str(w_title)}",
                         app_resolution=f"{int(w_width)}x{int(w_height)}+0+0",
                         app_verbose=w_verbose,
                         app_fullscreen=bool(w_fullscreen))

    def _create_frames(self) -> None:
        """
        create frames inside window
        :return: None
        """
        background_color = '#000000'
        height = self.frame_height
        width = self.frame_width

        self.frame = tk.Frame(self.window, bg=background_color, height=height, width=width)
        self.frame.grid(column=0, row=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def _update_widget(self, update_after: int = 60000) -> None:
        super()._update_widget(update_after_milliseconds=int(update_after))

        weather_metrics = OpenWeather()
        print(weather_metrics.get_weather_metrics())

        self.label_date.config(text=TimeMetrics())
        self.label_host.config(text=HostMetrics())

        self.window.after(int(update_after), self._update_widget)
