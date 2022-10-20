import tkinter as tk
import tkinter.font as tkf
from PIL import Image, ImageTk


class LCARS:

    def __init__(self, fullscreen: bool = False) -> None:
        self.fullscreen = bool(fullscreen)

        self.window = tk.Tk()
        self._config_window()
        self._create_frames()
        self._add_widgets()

        self.window.mainloop()

    def _config_window(self) -> None:
        self.window.title('LCARS SQUARE')
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.window.geometry('720x720+0+0')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.config(bg='black')
        self.window.protocol('WM_DELETE_WINDOW', self._on_closing)
        self.window.bind('<Escape>', self._exit)

        if self.fullscreen:
            self.window.config(cursor='none')
            self.window.attributes("-fullscreen", True)

    def _create_frames(self) -> None:
        pass

    def _add_widgets(self) -> None:
        pass

    def _on_closing(self) -> None:
        self._exit('close application by mouse')

    def _exit(self, event) -> None:
        self.window.destroy()


if __name__ == '__main__':
    LCARS()
