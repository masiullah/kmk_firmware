from micropython import const

from kmk.keys import make_argumented_key
from kmk.modules import Module


class ModHoldTapMode:
    AUTO = const(1)
    TIMEOUT = const(2)
    LAYER = const(2)


class ModHoldTapValidator:
    def __init__(self, kc, mod, mode=ModHoldTapMode.AUTO, timeout=2000):
        self.kc = kc
        self.mod = mod
        self.mode = mode
        self.timeout = timeout


class ModHoldTap(Module):
    def __init__(self):
        self._timeout_key = False
        self._mht_active = False
        self.mht_key = None
        make_argumented_key(
            names=('MHT',),
            validator=ModHoldTapValidator,
        )

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if isinstance(key.meta, ModHoldTapValidator):
            layer_id = keyboard.active_layers[0]
            self.mht_key = key
            if is_pressed:
                keyboard.process_key(key.meta.mod, is_pressed)
                self._mht_active = True
                if ModHoldTapMode.AUTO or ModHoldTapMode.TIMEOUT:
                    if layer_id == 0:
                        self.discard_timeout(keyboard)
            keyboard.process_key(key.meta.kc, is_pressed)
            if ModHoldTapMode.AUTO or ModHoldTapMode.TIMEOUT:
                if not is_pressed and layer_id == 0:
                    self.request_timeout(keyboard, key)
        elif self._mht_active:
            self.discard_timeout(keyboard)
            self.perform_timeout(keyboard, self.mht_key)

        return key

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def perform_timeout(self, keyboard, key):
        keyboard.process_key(key.meta.mod, False)
        self._mht_active = False
        self._timeout_key = False

    def request_timeout(self, keyboard, key):
        self._timeout_key = keyboard.set_timeout(
            key.meta.timeout, lambda: self.perform_timeout(keyboard, key)
        )

    def discard_timeout(self, keyboard):
        if self._timeout_key:
            keyboard.cancel_timeout(self._timeout_key)
            self._timeout_key = False
