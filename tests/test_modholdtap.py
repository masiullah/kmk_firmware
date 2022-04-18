import unittest

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modholdtap import ModHoldTap, ModHoldTapMode
from tests.keyboard_test import KeyboardTest


class TestWindowTab(unittest.TestCase):
    def test_basic_kmk_keyboard(self):

        keyboard = KeyboardTest(
            [ModHoldTap(), Layers()],
            [
                [
                    KC.MHT(KC.TAB, KC.LCTL, ModHoldTapMode.TIMEOUT, timeout=500),
                    KC.B,
                    KC.MO(1),
                    KC.LT(1, KC.C),
                    KC.E,
                    KC.F,
                ],
                [
                    KC.MHT(kc=KC.TAB, mod=KC.LGUI, timeout=500, mode=ModHoldTapMode.LAYER),
                    KC.B,
                    KC.MO(2),
                    KC.N4,
                    KC.N5,
                ],
                [KC.A, KC.B, KC.N3, KC.N4, KC.N5],
            ],
            debug_enabled=False,
        )

        keyboard.test(
            'basic test',
            [
                (0, True),
                (0, False),
                100,
                (0, True),
                200,
                (0, False),
                510,
                (1, True),
                (1, False),
            ],
            [
                {KC.LCTRL, KC.TAB},
                {KC.LCTRL},
                {KC.LCTRL, KC.TAB},
                {KC.LCTRL},
                {},
                {KC.B},
                {},
            ],
        )

        keyboard.test(
            'basic test2',
            [
                (0, True),
                (0, False),
                100,
                (0, True),
                200,
                (0, False),
                100,
                (1, True),
                (1, False),
            ],
            [
                {KC.LCTRL, KC.TAB},
                {KC.LCTRL},
                {KC.LCTRL, KC.TAB},
                {KC.LCTRL},
                {KC.B},
                {},
            ],
        )

        keyboard.test(
            'basic test with MO',
            [
                (2, True),
                200,
                (0, True),
                50,
                (0, False),
                (1, True),
                (1, False),
                (2, False),
                100,
                (1, True),
                (1, False),
            ],
            [
                {KC.LGUI, KC.TAB},
                {KC.LGUI},
                {KC.B},
                {},
                {KC.B},
                {},
            ],
        )

        keyboard.test(
            'basic test with LT',
            [
                (3, True),
                320,
                (0, True),
                50,
                (0, False),
                (1, True),
                (1, False),
                (3, False),
                100,
                (1, True),
                (1, False),
            ],
            [
                {KC.LGUI, KC.TAB},
                {KC.LGUI},
                {KC.B},
                {},
                {KC.B},
                {},
            ],
        )


if __name__ == '__main__':
    unittest.main()
