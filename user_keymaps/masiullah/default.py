from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.lock_status import LockStatus
from kmk.modules.capsword import CapsWord
from kmk.modules.swap_keys import SwapKeys


keyboard = KMKKeyboard()
keyboard.debug_enabled = True

caps_word = CapsWord()
swap_keys = SwapKeys()

split = Split(use_pio=True)
layers_ext = Layers()
keyboard.modules = [layers_ext, split, caps_word, swap_keys]

encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

keyboard.keymap = [
    [  # QWERTY
        KC.Q,           KC.W,           KC.E,           KC.R,           KC.T,           KC.Y,           KC.U,           KC.I,           KC.O,           KC.P,  \
        KC.A,           KC.S,           KC.D,           KC.F,           KC.A,           KC.H,           KC.J,           KC.K,           KC.L,           KC.QUOT, \
        KC.Z,           KC.X,           KC.C,           KC.V,           KC.B,           KC.N,           KC.M,           KC.COMM,        KC.DOT,        KC.SLSH, \
                                        KC.CW,          KC.LGUI,        KC.LCTL,        KC.CG_SWAP,     KC.CG_NORM,     KC.CG_TOGG,
    ],
    [  # QWERTY
        KC.Q,           KC.W,           KC.E,           KC.R,           KC.T,           KC.Y,           KC.U,           KC.I,           KC.O,           KC.P,  \
        KC.A,           KC.S,           KC.D,           KC.F,           KC.A,           KC.H,           KC.J,           KC.K,           KC.L,           KC.QUOT, \
        KC.Z,           KC.X,           KC.C,           KC.V,           KC.B,           KC.N,           KC.M,           KC.COMM,        KC.DOT,        KC.SLSH, \
                                        KC.CW,          KC.LGUI,        KC.LCTL,        KC.CG_SWAP,     KC.CG_NORM,     KC.CG_TOGG,
    ]
]

encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),
)
keyboard.modules.append(encoder_handler)


if __name__ == '__main__':
    keyboard.go()
