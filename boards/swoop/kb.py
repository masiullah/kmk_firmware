import board

from kmk.extensions.lock_status import LockStatus
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):

    col_pins = (
        board.SCK,
        board.A0,
        board.A1,
        board.A2,
        board.A3,
    )
    row_pins = (
        board.D4,
        board.D5,
        board.D6,
        board.D7,
    )
    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = board.D13
    data_pin2 = board.D12
    encoder_pin_0 = board.D9
    encoder_pin_1 = board.D8
    i2c = board.I2C

    # flake8: noqa
    # fmt: off
    coord_mapping = [
     0,  1,  2,  3,  4,  20, 21, 22, 23, 24,
     5,  6,  7,  8,  9,  25, 26, 27, 28, 29,
    10, 11, 12, 13, 14,  30, 31, 32, 33, 34,
            17, 18, 19,  35, 36, 37,
    ]
    # fmt: on
