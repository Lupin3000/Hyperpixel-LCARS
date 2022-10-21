import logging
import tkinter as tk
from typing import Literal


class LcarsBase:
    """
    base lcars class for tkinter application
    """

    def __init__(self,
                 title: str = 'LCARS',
                 resolution: str = '720x720+0+0',
                 fullscreen_mode: bool = False,
                 verbose_mode: Literal[1, 2, 3] = 1) -> None:
        """
        initialize tkinter application and start loop
        :param title: set application title
        :param resolution: set application resolution
        :param fullscreen_mode: set application fullscreen mode (True or False)
        :param verbose_mode: set application log level (3 = Debug, 2 = Info, 1 = Error)
        """
        if verbose_mode == 3:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
        elif verbose_mode == 2:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
        else:
            logging.basicConfig(level=logging.ERROR,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')

        self.__logger = logging.getLogger(__name__)

        self.window = tk.Tk()
        self._config_window(win_title=title, win_resolution=resolution, win_fullscreen=fullscreen_mode)
        self._create_frames()
        self._add_widgets()

        self.window.mainloop()

    def _config_window(self,
                       win_title: str,
                       win_resolution: str,
                       win_fullscreen: bool) -> None:
        """
        configure tkinter window
        :param win_title: window title
        :param win_resolution: window resolution
        :param win_fullscreen: window fullscreen
        :return: None
        """
        self.__logger.debug(f"app title: {win_title}, resolution: {win_resolution}, fullscreen: {win_fullscreen}")

        background_color = '#000000'

        self.window.title(str(win_title))
        self.window.geometry(str(win_resolution))
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.config(bg=background_color)

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.window.protocol('WM_DELETE_WINDOW', self._on_closing)
        self.window.bind('<Escape>', self._exit)

        if bool(win_fullscreen):
            self.window.config(cursor='none')
            self.window.attributes("-fullscreen", True)
        else:
            self.window.attributes('-topmost', 1)

    def _create_frames(self) -> None:
        """
        create tkinter frames
        :return: None
        """
        pass

    def _add_widgets(self) -> None:
        """
        add tkinter widgets
        :return: None
        """
        pass

    def _update_widget(self,
                       update_after_milliseconds: int = 60000) -> None:
        """
        update tkinter widgets
        :param update_after_milliseconds: update tkinter widget
        :return: None
        """
        self.__logger.info(f"app update: {update_after_milliseconds} milliseconds")

    def _on_closing(self) -> None:
        """
        catch tkinter mouse close window event
        :return: None
        """
        self._exit('<Mouse event>')

    def _exit(self,
              event) -> None:
        """
        exit and close tkinter window
        :param event: events which trigger exit
        :return: None
        """
        self.__logger.info(f"app exit: {event}")

        self.window.destroy()
