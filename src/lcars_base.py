import tkinter as tk


class LcarsBase:
    """
    base lcars class for tkinter application
    """

    def __init__(self,
                 title: str = 'LCARS',
                 resolution: str = '720x720+0+0',
                 fullscreen: bool = False) -> None:
        """
        initialize tkinter application and start loop
        :param title: set application title
        :param resolution: set application resolution
        :param fullscreen: set application fullscreen mode
        """
        self.window = tk.Tk()
        self._config_window(win_title=title, win_resolution=resolution, win_fullscreen=fullscreen)
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

    def _on_closing(self) -> None:
        """
        catch tkinter mouse close window event
        :return: None
        """
        self._exit('close application by mouse event')

    def _exit(self,
              event: str) -> None:
        """
        exit and close tkinter window
        :param event: events which trigger exit
        :return: None
        """
        print(f"[INFO]: {event}")
        self.window.destroy()
