import socket
import time


class HostMetrics:
    """
    module class to get hostname
    """

    def __init__(self) -> None:
        """
        initialize module class for hostname
        """
        self.hostname = str(socket.gethostname())

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
        self.current_date = str(time.strftime('%d-%m%Y'))

    def __str__(self) -> str:
        """
        return string of time (in specific format)
        :return: str
        """
        return self.current_date
