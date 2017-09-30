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
            # MENU BUTTONS
            # These regions aren't accurate.
            "MAIN_MENU_CLICK_MOUSE_PLAY": (357, 508, 579, 767),
            "MODE_MENU_SURVIVAL": (93, 658, 629, 1108),
            # SURVIVAL MENU BUTTONS
            "SURVIVAL_MENU_BUTTON_TOP": (281, 458, 349, 822),
            "SURVIVAL_PRE_GAME_START_BUTTON": (81, 897, 124, 1085),
            # GAME BUTTONS
            "GAME_OVER_SCORE_BUTTON": (414, 1037, 537, 1148),

            # These zones are used only for capturing sprites.
            # PUCH ZONE
            # "PUNCH_ZONE_LEFT": (350, 536, 414, 608),
            # "PUNCH_ZONE_RIGHT": (350, 672, 414, 744),
            #
            # "CROWN": (280, 255, 320, 1020),
            #
            # "PUNCH_ZONE_BRAWLER_LEFT": (211, 334, 270, 410),
            # "PUNCH_ZONE_BRAWLER_RIGHT": (211, 870, 270, 946),
            #
            # "PUNCH_ZONE_BRAWLER_LEFT_ZO": (140, 437, 179, 482),
            # "PUNCH_ZONE_BRAWLER_RIGHT_ZO": (140, 792, 179, 843)
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
