# ModHoldTap
This module allows to immitate the behaviour of ATL+TAB or CMD+TAB, etc. Basically, it will result in mod hold followed by key press and release and the mod will release with a timeout(default 2s) or any other key press including layer change

## Enabling the module
```python
from kmk.module.modholdtap import ModHoldTap
modholdtap = ModHoldTap()
keyboard.modules.append(modholdtap)
keyboard.keymap = [
    [
        KC.MHT(KC.TAB, KC.LALT),
    ],
]
```

## Keycodes

|Key                     |Description                                    |
|------------------------|-----------------------------------------------|
|`KC.MHT(KC.key, KC.mod)`|Enables/disables capsword                      |

## Custom ModHoldTap Behavior
The full ModHoldTap signature is as follows:
```python
KC.MT(KC.KEY, KC.MOD, mode=ModHoldTapMode.AUTO, timeout=2000)
KC.KEY = key
KC.MOD = mod
mode = ModHoldTapMode.LAYER (mod release on layer change or key press), ModHoldTapMode.TIMEOUT (mod release on timeout or key press), ModHoldTapMode.AUTO (works as TIMEOUT mode if the key is used on the default layer otherwise works in LAYER mode if the key is on any other layer)
timeout = time in ms for releasing the mod