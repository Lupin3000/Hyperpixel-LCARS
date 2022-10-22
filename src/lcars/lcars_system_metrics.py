import socket
import time
import psutil


class HostMetrics:
    """
    module class to get hostname
    """

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


class TimeMetrics:
    """
    module class to get time
    """

    def __init__(self) -> None:
        """
        initialize module class for time
        """
        self.current_date = f"{time.strftime('%d-%m%Y')}"

    def __str__(self) -> str:
        """
        return string of time (in specific format)
        :return: str
        """
        return self.current_date


class RamMetrics:

    def __init__(self) -> None:
        """
        initialize module class for ram
        """
        ram = psutil.virtual_memory()
        self.info = f"{ram.total >> 30}-{ram.available >> 30}{ram.used >> 30}{ram.free >> 30}"

    def __str__(self) -> str:
        """
        return string of ram (in specific format)
        :return: str
        """
        return self.info
