import platform
import socket
import time

import psutil

"""
Helper classes to get some system metrics (some in specific format)
"""


class SystemMetrics:
    def __init__(self) -> None:
        """
        initialize module class for system metrics
        """
        self.hostname = f"{socket.gethostname()}"
        self.os = f"{platform.uname().system}"
        self.ram = f"{psutil.virtual_memory().total >> 20}"


class DateMetrics:

    def __init__(self) -> None:
        """
        initialize module class for date
        """
        self.current_date = f"{time.strftime('%d-%m-%Y')}"

    def __str__(self) -> str:
        """
        return string of date (in specific format)
        :return: str
        """
        return self.current_date


class TimeMetrics:

    def __init__(self) -> None:
        """
        initialize module class for time
        """
        self.current_time = f"{time.strftime('%H-%M')}"

    def __str__(self) -> str:
        """
        return string of time (in specific format)
        :return: str
        """
        return self.current_time
