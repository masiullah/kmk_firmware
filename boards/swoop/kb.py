import board
import busio

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [
            MatrixScanner(
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                columns_to_anodes=DiodeOrientation.COL2ROW,
            ),
            RotaryioEncoder(
                pin_a=board.D9,
                pin_b=board.D8,
                divisor=4,
            ),
        ]

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

    data_pin = board.D1

    i2c = board.I2C

    SCL = board.D3
    SDA = board.D2

    # flake8: noqa
    # fmt: off
    coord_mapping = [
     0,  1,  2,  3,  4,  26, 25, 24, 23, 22,
     5,  6,  7,  8,  9,  31, 30, 29, 28, 27,
    10, 11, 12, 13, 14,  36, 35, 34, 33, 32,
            17, 18, 19,  41, 40, 39,
    20, 21,                          43, 42,
    ]
    # fmt: on
