import logging
import tkinter as tk


class LcarsBase:
    """
    base lcars class for tkinter application
    """

    _DEFAULT_BACKGROUND_COLOR = '#000000'

    def __init__(self, app_title: str, app_resolution: str, app_verbose: int, app_fullscreen: bool) -> None:
        """
        initialize and start loop of tkinter application with title, resolution, verbose and fullscreen mode
        :param app_title: set application title
        :param app_resolution: set application resolution
        :param app_fullscreen: set application fullscreen mode (True or False)
        :param app_verbose: set application log level (3 = Debug, 2 = Info, 1 = Error)
        """
        # configure logging
        if app_verbose == 3:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
        elif app_verbose == 2:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
        else:
            logging.basicConfig(level=logging.ERROR,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')

        self.__logger = logging.getLogger(__name__)

        # greate window
        self.window = tk.Tk()
        self.__config_window(title=app_title, resolution=app_resolution, fullscreen=app_fullscreen)

        self._create_frames()
        self._add_widgets()

        self.window.mainloop()

    def __config_window(self, title: str, resolution: str, fullscreen: bool) -> None:
        """
        configure tkinter application window
        :param title: window title
        :param resolution: window resolution
        :param fullscreen: window fullscreen
        :return: None
        """
        self.__logger.debug(f"app title: {title}, resolution: {resolution}, fullscreen: {fullscreen}")

        self.window.title(str(title))
        self.window.geometry(str(resolution))
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.config(bg=self._DEFAULT_BACKGROUND_COLOR)

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.window.protocol('WM_DELETE_WINDOW', self.__on_closing)
        self.window.bind('<Escape>', self._exit)

        if bool(fullscreen):
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

    def _update_widget(self, update_after_milliseconds: int = 60000) -> None:
        """
        update tkinter widgets after specific milliseconds
        :param update_after_milliseconds: milliseconds to reload
        :return: None
        """
        self.__logger.info(f"app update: {update_after_milliseconds} milliseconds")

    def __on_closing(self) -> None:
        """
        catch tkinter mouse close window event
        :return: None
        """
        self._exit('<Mouse event>')

    def _exit(self, event) -> None:
        """
        exit and close tkinter window
        :param event: events which trigger exit
        :return: None
        """
        self.__logger.info(f"app exit: {event}")

        self.window.destroy()
