from serpent.game import Game

from .api.api import OneFingerDeathPunchAPI

from serpent.utilities import Singleton


class SerpentOneFingerDeathPunchGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "One Finger Death Punch"

        kwargs["app_id"] = "264200"
        kwargs["app_args"] = None


        super().__init__(**kwargs)

        self.api_class = OneFingerDeathPunchAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "PAUSE_BUTTON": (0, 0, 32, 57),
            # SURVIVAL MENU BUTTONS
            "SURVIVAL_MENU_BUTTON_TOP": (281, 458, 349, 822)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
