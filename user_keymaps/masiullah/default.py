from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.cg_swap import CgSwap
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

caps_word = CapsWord(False)
cg_swap = CgSwap()
split = Split(use_pio=True)
modtap = ModTap()
layer = Layers()
keyboard.modules = [split, layer, caps_word, cg_swap, modtap]

encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

KC_Z = KC.MT(KC.Z,KC.LALT) 
KC_ENT = KC.MT(KC.ENT,KC.RALT) 
KC_X = KC.MT(KC.X,KC.LCTL) 
KC_DOT = KC.MT(KC.DOT,KC.RCTL) 
KC_C = KC.MT(KC.C,KC.LGUI) 
KC_COMM = KC.MT(KC.COMM,KC.RGUI) 
KC_V = KC.MT(KC.V,KC.LSFT) 
KC_M = KC.MT(KC.M,KC.RSFT) 

KC_SYM_TAB = KC.LT(3, KC.TAB)
KC_NAV_SPC = KC.LT(1, KC.SPC)
KC_OS_LSFT = KC.OS(KC.LSFT)
KC_NUM_BSP = KC.LT(2, KC.BKDL)
KC_CMNT1 = KC.LALT(KC.LGUI(KC.SLSH))
KC_CMNT2 = KC.LGUI(KC.SLSH)
KC_LFT_SEL = KC.LALT(KC.LSFT(KC.LEFT))
KC_RGT_SEL = KC.LALT(KC.LSFT(KC.RIGHT))


# flake8: noqa
# fmt: off
keyboard.keymap = [
    [  # BASE 
        KC.Q,           KC.W,           KC.E,           KC.R,           KC.T,           KC.Y,           KC.U,           KC.I,           KC.O,           KC.P,  
        KC.A,           KC.S,           KC.D,           KC.F,           KC.G,           KC.H,           KC.J,           KC.K,           KC.L,           KC.QUOT, 
        KC_Z,           KC_X,           KC_C,           KC_V,           KC.B,           KC.N,           KC_M,           KC_COMM,        KC_DOT,         KC_ENT, 
                                        KC.LEADER,      KC_SYM_TAB,     KC_NAV_SPC,     KC_OS_LSFT,     KC_NUM_BSP,     KC.MUTE,
    ],
    [  # NAV
        KC.ESC,         KC.TAB,         KC_CMNT1,       KC_CMNT2,       KC.TRNS,        KC.INS,         KC.HOME,        KC.UP,          KC.END,         KC.BKDL,  
        KC_ALT_TAB,     KC_CTL_TAB,     KC_CMD_TAB,     KC_CMD_GRV,     KC.TRNS,        KC.ENT,         KC.LEFT,        KC.DOWN,        KC.RGHT,        KC.PSCR, 
        KC.CW,          KC.CAPS,        KC_LFT_SEL,     KC_RGT_SEL,     KC.TRNS,        KC.BSPC,        KC.DEL,         KC.PGDN,        KC.PGUP,        KC.ENT, 
                                        KC.TRNS,        KC.CW,          KC.TRNS,        KC.LSFT,        KC.BKDL,        KC.TRNS,
    ]
    [  # NUM
        KC.N1,          KC.N2,          KC.N3,          KC.N4,          KC.N5,          KC.N6,          KC.N7,          KC.N8,          KC.N9,          KC.N0,  
        KC.F1,          KC.F2,          KC.F3,          KC.F4,          KC.F5,          KC.F6,          KC.MINS,        KC.EQL,         KC.LBRC,        KC.RBRC, 
        KC.F7,          KC.F8,          KC.F9,          KC.F10,         KC.F11,         KC.F12,         KC.SLSH,        KC.SCLN,        KC.BSLS,        KC.GRV, 
                                        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,
    ]
]
# fmt: on
encoder_handler.map = (((KC.VOLD, KC.VOLU),),)
keyboard.modules.append(encoder_handler)


if __name__ == '__main__':
    keyboard.go()
