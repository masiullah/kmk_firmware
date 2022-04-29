from supervisor import runtime

from kb import KMKKeyboard

from kmk.extensions.peg_oled_display import (
    Oled,
    OledData,
    OledDisplayMode,
    OledReactionType,
)
from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.cg_swap import CgSwap
from kmk.modules.combos import Chord, Combos, Sequence
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot
from kmk.modules.split import Split
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
keyboard.debug_enabled = False

caps_word = CapsWord(False)
cg_swap = CgSwap()
split = Split(use_pio=True)
modtap = ModTap()
layer = Layers()
tapdance = TapDance()
oneshot = OneShot()
combos = Combos()
sticky_mod = StickyMod()

keyboard.modules = [
    modtap,
    layer,
    tapdance,
    oneshot,
    combos,
    split,
    caps_word,
    cg_swap,
    sticky_mod,
]


KC_Z = KC.TD(KC.Z, KC.LALT)
KC_ENT = KC.MT(KC.ENT, KC.RALT)
KC_X = KC.MT(KC.X, KC.LCTL)
KC_DOT = KC.MT(KC.DOT, KC.RCTL)
KC_C = KC.MT(KC.C, KC.LGUI)
KC_COMM = KC.MT(KC.COMM, KC.RGUI)
KC_V = KC.MT(KC.V, KC.LSFT)
KC_M = KC.MT(KC.M, KC.RSFT)
KC_SYM_TAB = KC.LT(3, KC.TAB, tap_time=120)
KC_NAV_SPC = KC.LT(1, KC.SPC, tap_time=120)
KC_OS_LSFT = KC.OS(KC.LSFT)
KC_NUM_BSP = KC.LT(2, KC.BSPC, tap_time=120)
KC_CMNT1 = KC.LALT(KC.LGUI(KC.SLSH))
KC_CMNT2 = KC.LGUI(KC.SLSH)
KC_LFT_SEL = KC.LALT(KC.LSFT(KC.LEFT))
KC_RGT_SEL = KC.LALT(KC.LSFT(KC.RIGHT))

KC_ALT_TAB = KC.SM(KC.TAB, KC.LALT)
KC_ALTSFT_TAB = KC.SM(KC.TAB, KC.LSFT(KC.LALT))
KC_CTL_TAB = KC.SM(KC.TAB, KC.LCTL)
KC_CTLSFT_TAB = KC.SM(KC.TAB, KC.LSFT(KC.LCTL))
KC_CMD_TAB = KC.SM(KC.TAB, KC.LGUI)
KC_CMDSFT_TAB = KC.SM(KC.TAB, KC.LSFT(KC.LGUI))
KC_CMD_GRV = KC.SM(KC.GRV, KC.LGUI)
KC_CMDSFT_GRV = KC.SM(KC.GRV, KC.LSFT(KC.LGUI))

KC_UNDO = KC.LGUI(KC.Z)
KC_REDO = KC.LSFT(KC.LGUI(KC.Z))


if runtime.usb_connected:
    oled_ext = Oled(
        OledData(
            corner_one={0: OledReactionType.STATIC, 1: ["L = "]},
            corner_two={0: OledReactionType.LAYER, 1: ["1", "2", "3", "4"]},
            corner_three={0: OledReactionType.LAYER, 1: ["BASE", "SFN", "NUM", "ADJ"]},
            corner_four={
                0: OledReactionType.LAYER,
                1: ["CW= 2", "numslock", "shifted", "leds"],
            },
        ),
        toDisplay=OledDisplayMode.TXT,
        flip=False,
    )
else:
    oled_ext = Oled(
        OledData(
            image={
                0: OledReactionType.LAYER,
                1: ["logo.bmp"],
            }
        ),
        toDisplay=OledDisplayMode.IMG,
        flip=False,
    )

keyboard.extensions.append(oled_ext)


# flake8: noqa
# fmt: off
keyboard.keymap = [
    [  # BASE 
        KC.Q,           KC.W,           KC.E,           KC.R,           KC.T,           KC.Y,           KC.U,           KC.I,           KC.O,           KC.P,  
        KC.A,           KC.S,           KC.D,           KC.F,           KC.G,           KC.H,           KC.J,           KC.K,           KC.L,           KC.QUOT, 
        KC_Z,           KC_X,           KC_C,           KC_V,           KC.B,           KC.N,           KC_M,           KC_COMM,        KC_DOT,         KC_ENT, 
                                        KC.LEADER,      KC_SYM_TAB,     KC_NAV_SPC,     KC_OS_LSFT,     KC_NUM_BSP,     KC.MUTE,
        KC_REDO,        KC_UNDO,                                                                                                        KC.VOLU,        KC.VOLD,
    ],
    [  # NAV
        KC.ESC,         KC.TAB,         KC_CMNT1,       KC_CMNT2,       KC.TRNS,        KC.INS,         KC.HOME,        KC.UP,          KC.END,         KC.BKDL,  
        KC.TAB,         KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.ENT,         KC.LEFT,        KC.DOWN,        KC.RGHT,        KC.PSCR, 
        KC.CW,          KC.CAPS,        KC_LFT_SEL,     KC_RGT_SEL,     KC.TRNS,        KC.BSPC,        KC.DEL,         KC.PGDN,        KC.PGUP,        KC.ENT, 
                                        KC.TRNS,        KC.CW,          KC.TRNS,        KC.LSFT,        KC.BKDL,        KC.TRNS,
        KC.VOLU,        KC.VOLD,                                                                                                        KC_CMD_TAB,     KC_CMDSFT_TAB,                   
    ],
    [  # NUM
        KC.N1,          KC.N2,          KC.N3,          KC.N4,          KC.N5,          KC.N6,          KC.N7,          KC.N8,          KC.N9,          KC.N0,  
        KC.F1,          KC.F2,          KC.F3,          KC.F4,          KC.F5,          KC.F6,          KC.MINS,        KC.EQL,         KC.LBRC,        KC.RBRC, 
        KC.F7,          KC.F8,          KC.F9,          KC.F10,         KC.F11,         KC.F12,         KC.SLSH,        KC.SCLN,        KC.BSLS,        KC.GRV, 
                                        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,
        KC_ALT_TAB,     KC_ALTSFT_TAB,                                                                                                  KC.VOLU,        KC.VOLD,
    ],
    [  # SYM
        KC.EXLM,        KC.AT,          KC.HASH,        KC.DLR,         KC.PERC,        KC.CIRC,        KC.AMPR,        KC.ASTR,        KC.LPRN,        KC.RPRN,  
        KC.F1,          KC.F2,          KC.F3,          KC.F4,          KC.F5,          KC.F6,          KC.UNDS,        KC.PLUS,        KC.LCBR,        KC.RCBR, 
        KC.F7,          KC.F8,          KC.F9,          KC.F10,         KC.F11,         KC.F12,         KC.QUES,        KC.COLN,        KC.PIPE,        KC.TILD, 
                                        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,        KC.TRNS,
        KC_ALT_TAB,     KC_ALTSFT_TAB,                                                                                                  KC_CMD_GRV,     KC_CMDSFT_GRV,
    ],
]
# fmt: on

if __name__ == '__main__':
    keyboard.go()
