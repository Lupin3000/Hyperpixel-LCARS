import tkinter as tk
import tkinter.font as tkf

from PIL import Image, ImageTk
from lcars.lcars_app_base import LcarsBase
from lcars.lcars_system_metrics import HostMetrics, DateMetrics, TimeMetrics, RamMetrics, PlatformMetrics
from lcars.lcars_weather import OpenWeather


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
        self.window_width = int(w_width)
        self.window_height = int(w_height)

        self.frames = dict()
        self.fonts = dict()
        self.colors = dict()

        self.label_time = None
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

    def _add_frames(self, count: int = 1) -> None:
        """
        create all frames inside application window
        :param count: frames to create as int
        :return: None
        """
        self.logger.debug(f"app > create {count} frames")

        for num in range(count):
            self.frames[num] = tk.Frame(self.window, bg=self._DEFAULT_BACKGROUND_COLOR)
            self.frames[num].rowconfigure(0, weight=1)
            self.frames[num].columnconfigure(0, weight=1)

        self.frames[0].grid(column=0, row=0)

    def _set_fonts(self, headline: int, paragraph_top: int, time: int, paragraph_bottom: int, sidebar: int) -> None:
        """
        create dictionary of font styles settings for arguments
        :param headline: set headline
        :param paragraph_top: set paragraph as tkf.Font
        :param time: set time as tkf.Font
        :param paragraph_bottom: set paragraph as tkf.Font
        :param sidebar: set sidebar as tkf.Font
        :return: None
        """
        self.logger.debug(f"app > set fonts")

        self.fonts = {
            'headline': tkf.Font(family='Okuda', weight='normal', size=int(headline)),
            'paragraph_top': tkf.Font(family='Okuda', weight='normal', size=int(paragraph_top)),
            'time': tkf.Font(family='Okuda', weight='normal', size=int(time)),
            'paragraph_bottom': tkf.Font(family='Okuda', weight='normal', size=int(paragraph_bottom)),
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
        self.logger.debug(f"app > set colors")

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
        set background image to frames[0] and place as label
        :param image_path: path to image as string
        :return: None
        """
        self.logger.debug(f"app > set background image")

        img_bg = Image.open(str(image_path))
        bg_bg = ImageTk.PhotoImage(img_bg)

        label_bg = tk.Label(self.frames[0], image=bg_bg, bg=self.colors['black'])
        label_bg.image = bg_bg
        label_bg.grid(column=0, row=0)

    def _update_widget(self, update_after: int = 60000) -> None:
        """
        update widget and set next reload
        :param update_after: time in milliseconds as int
        :return: None
        """
        self.logger.debug(f"app > update widgets")

        weather_metrics = OpenWeather()
        weather_measures = weather_metrics.get_weather_metrics()

        self.label_temperature.config(text=f"T: {weather_measures['temperature']}")
        self.label_pressure.config(text=f"P: {weather_measures['pressure']}")
        self.label_humidity.config(text=f"H: {weather_measures['humidity']}")
        self.label_wind.config(text=f"W: {weather_measures['wind']}")

        self.label_time.config(text=TimeMetrics())
        self.label_date.config(text=DateMetrics())
        self.label_host.config(text=HostMetrics())
        self.label_ram.config(text=RamMetrics())
        self.label_os.config(text=PlatformMetrics())

        self.window.after(int(update_after), self._update_widget)
