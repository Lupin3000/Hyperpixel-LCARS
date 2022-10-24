import platform
import socket
import time

import psutil

"""
Helper classes to get some system metrics (some in specific format)
"""


class HostMetrics:
    def __init__(self) -> None:
        """
        initialize module class for hostname
        """
        self.hostname = f"{socket.gethostname()}"

    def __str__(self) -> str:
        """
        return string of hostname
        :return: str
        """
        return self.hostname


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


class RamMetrics:

    def __init__(self) -> None:
        """
        initialize module class for ram
        """
        ram = psutil.virtual_memory()
        self.info = f"{ram.total >> 30}-{ram.available >> 30}{ram.used >> 30}-{ram.free >> 30}"

    def __str__(self) -> str:
        """
        return string of ram (in specific format)
        :return: str
        """
        return self.info


class PlatformMetrics:
    def __init__(self) -> None:
        """
        initialize module class for platform name
        """
        self.osname = f"{platform.uname().system}"

    def __str__(self) -> str:
        """
        return string of os name
        :return: str
        """
        return self.osname
