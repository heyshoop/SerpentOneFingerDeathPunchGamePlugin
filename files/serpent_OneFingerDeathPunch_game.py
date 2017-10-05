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

            #END HIGHSCORES LETTERS
            "HS_LETTER_A": (343, 120, 368, 140),
            "HS_LETTER_B": (343, 156, 368, 176),
            "HS_LETTER_C": (343, 197, 368, 217),
            "HS_LETTER_D": (343, 236, 368, 256),
            "HS_LETTER_E": (343, 277, 368, 297),
            "HS_LETTER_F": (343, 311, 368, 331),
            "HS_LETTER_G": (343, 353, 368, 373),
            "HS_LETTER_H": (343, 393, 368, 413),
            "HS_LETTER_I": (343, 432, 368, 452),
            "HS_LETTER_J": (343, 473, 368, 493),
            "HS_LETTER_K": (343, 508, 368, 528),
            "HS_LETTER_L": (343, 548, 368, 568),
            "HS_LETTER_M": (343, 590, 368, 610),
            "HS_LETTER_N": (343, 627, 368, 647),
            "HS_LETTER_O": (343, 671, 368, 691),
            "HS_LETTER_P": (343, 708, 368, 728),
            "HS_LETTER_Q": (343, 749, 368, 769),
            "HS_LETTER_R": (343, 787, 368, 807),
            "HS_LETTER_S": (343, 787, 368, 807),
            "HS_LETTER_T": (343, 864, 368, 884),
            "HS_LETTER_U": (343, 906, 368, 926),
            "HS_LETTER_V": (343, 941, 368, 961),
            "HS_LETTER_W": (343, 978, 368, 998),
            "HS_LETTER_X": (343, 1024, 368, 1044),
            "HS_LETTER_Y": (343, 1059, 368, 1079),
            "HS_LETTER_Z": (343, 1100, 368, 1120),
            "HS_BTN_BACK": (425, 537, 491, 742),
            "HS_OK": (552, 619, 608, 672)

            # These zones are used only for capturing sprites.
            # PUCH ZONE
            # "PUNCH_ZONE_LEFT": (350, 536, 360, 608),
            # "PUNCH_ZONE_RIGHT": (350, 672, 360, 744),
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
