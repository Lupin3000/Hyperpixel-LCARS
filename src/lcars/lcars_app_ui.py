import tkinter as tk
import tkinter.font as tkf
from PIL import Image, ImageTk

from src.lcars.lcars_app_base import LcarsBase
from src.lcars.lcars_system_metrics import HostMetrics, TimeMetrics, RamMetrics, PlatformMetrics
from src.lcars.lcars_weather import OpenWeather


class LcarsUi(LcarsBase):

    def __init__(self, w_width: int, w_height: int, w_title: str, w_verbose: int, w_fullscreen: bool = False) -> None:
        """
        initialize window setting for resolution (width, height), title, verbose and fullscreen mode
        :param w_width: base frame and window resolution width
        :param w_height: base frame and window resolution height
        :param w_title: set window title
        :param w_verbose: set window verbose log level (3 = Debug, 2 = Info, 1 = Error)
        :param w_fullscreen: set window fullscreen mode (True or False)
        """
        self.frames = None
        self.frame_width = int(w_width)
        self.frame_height = int(w_height)

        self.fonts = None
        self.colors = None

        self.label_date = None
        self.label_host = None
        self.label_ram = None
        self.label_os = None

        self.label_temperature = None
        self.label_pressure = None
        self.label_humidity = None
        self.label_wind = None

        super().__init__(app_title=f"LCARS {str(w_title)}",
                         app_resolution=f"{int(w_width)}x{int(w_height)}+0+0",
                         app_verbose=w_verbose,
                         app_fullscreen=bool(w_fullscreen))

    def _create_frames(self) -> None:
        """
        create all frames inside application window
        :return: None
        """
        self.frames = tk.Frame(self.window,
                               bg=self._DEFAULT_BACKGROUND_COLOR,
                               height=self.frame_height,
                               width=self.frame_width)

        self.frames.grid(column=0, row=0)
        self.frames.rowconfigure(0, weight=1)
        self.frames.columnconfigure(0, weight=1)

    def _set_fonts(self, headline: int, paragraph: int, sidebar: int) -> None:
        """
        create dictionary of font styles settings for arguments
        :param headline: set headline
        :param paragraph: set paragraph as tkf.Font
        :param sidebar: set sidebar as tkf.Font
        :return: None
        """
        self.fonts = {
            'headline': tkf.Font(family='Okuda', weight='normal', size=int(headline)),
            'paragraph': tkf.Font(family='Okuda', weight='normal', size=int(paragraph)),
            'side_bar': tkf.Font(family='Okuda', weight='normal', size=int(sidebar))
        }

    def _set_colors(self, headline: str = '#FFFFFF', paragraph: str = '#FFFFFF',
                    white: str = '#FFFFFF', black: str = '#000000',
                    red: str = '#FF0000', green: str = '00FF00', blue: str = '#0000FF') -> None:
        """
        set basic color palette as dictionary
        :param headline: set HEX color code for element
        :param paragraph: set HEX color code for element
        :param white: set HEX color code for base color
        :param black: set HEX color code for base color
        :param red: set HEX color code for base color
        :param green: set HEX color code for base color
        :param blue: set HEX color code for base color
        :return: None
        """
        self.colors = {
            'headline': str(headline),
            'paragraph': str(paragraph),
            'white': str(white),
            'black': str(black),
            'red': str(red),
            'green': str(green),
            'blue': str(blue)
        }

    def _set_background(self, image_path: str) -> None:
        """
        set background image and place as label
        :param image_path: path to image as string
        :return: None
        """
        img_bg = Image.open(str(image_path))
        bg_bg = ImageTk.PhotoImage(img_bg)

        label_bg = tk.Label(self.frames, image=bg_bg, bg=self.colors['black'])
        label_bg.image = bg_bg
        label_bg.grid(column=0, row=0)

    def _update_widget(self, update_after: int = 60000) -> None:
        """
        update widget and set next reload
        :param update_after: time in milliseconds as int
        :return: None
        """
        super()._update_widget(update_after_milliseconds=int(update_after))

        weather_metrics = OpenWeather()
        weather_measures = weather_metrics.get_weather_metrics()

        self.label_temperature.config(text=f"T: {weather_measures['temperature']}")
        self.label_pressure.config(text=f"P: {weather_measures['pressure']}")
        self.label_humidity.config(text=f"H: {weather_measures['humidity']}")
        self.label_wind.config(text=f"W: {weather_measures['wind']}")

        self.label_date.config(text=TimeMetrics())
        self.label_host.config(text=HostMetrics())
        self.label_ram.config(text=RamMetrics())
        self.label_os.config(text=PlatformMetrics())

        self.window.after(int(update_after), self._update_widget)
