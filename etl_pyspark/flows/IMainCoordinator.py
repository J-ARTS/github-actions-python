import logging
from abc import ABC, abstractmethod


class IMainCoordinator(ABC):

    def __init__(self):
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    @abstractmethod
    def start(self) -> None:
        pass
