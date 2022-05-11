
from racetime_bot import Bot

from handler import RandoHandler
from pm64r import PM64R


class RandoBot(Bot):
    """
    RandoBot base class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pm64r = PM64R()

    def get_handler_class(self):
        return RandoHandler

    def get_handler_kwargs(self, *args, **kwargs):
        return {
            **super().get_handler_kwargs(*args, **kwargs),
            'pm64r': self.pm64r,
        }