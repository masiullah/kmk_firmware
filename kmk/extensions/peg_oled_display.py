import busio
import gc
import microcontroller

import adafruit_displayio_ssd1306
import displayio
import terminalio
from adafruit_display_text import label

from kmk.extensions import Extension


class OledDisplayMode:
    TXT = 0
    IMG = 1


class OledReactionType:
    STATIC = 0
    LAYER = 1


class OledData:
    def __init__(
        self,
        image=None,
        corner_one=None,
        corner_two=None,
        corner_three=None,
        corner_four=None,
    ):
        if image:
            self.data = [image]
        elif corner_one and corner_two and corner_three and corner_four:
            self.data = [corner_one, corner_two, corner_three, corner_four]


class Oled(Extension):
    def __init__(
        self,
        views,
        capsword=None,
        toDisplay=OledDisplayMode.TXT,
        oWidth=128,
        oHeight=32,
        flip: bool = True,

    ):
        displayio.release_displays()
        self.rotation = 180 if flip else 0
        self._views = views.data
        self._toDisplay = toDisplay
        self._width = oWidth
        self._height = oHeight
        self._prevLayers = 0
        self._cw_active = False
        self._capsword = capsword
        gc.collect()

    def returnCurrectRenderText(self, layer, singleView):
        text = ''
        # for now we only have static things and react to layers. But when we react to battery % and wpm we can handle the logic here
        if singleView[0] == OledReactionType.STATIC:
            text = singleView[1][0]
        if singleView[0] == OledReactionType.LAYER:
            text = singleView[1][layer]

        return text if len(text) <= 5 else text[0:5]

    def renderOledTextLayer(self, layer):

        splash = displayio.Group()
        self._display.show(splash)
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[0]),
                color=0xFFFFFF,
                x=125,
                y=0,
                label_direction='DWR',
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[1]),
                color=0xFFFFFF,
                x=125,
                y=25,
                label_direction='DWR',
            )
        )

        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[2]),
                color=0xFFFFFF,
                x=110,
                y=0,
                label_direction='DWR',
            )
        )
        print(self._capsword._cw_active)
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[3]) + str(self._capsword._cw_active),
                color=0xFFFFFF,
                x=95,
                y=0,
                label_direction='DWR',
            )
        )

        splash.append(
            label.Label(
                terminalio.FONT,
                text='T=' + str(int(microcontroller.cpu.temperature)) + 'C',
                color=0xFFFFFF,
                x=80,
                y=0,
                label_direction='DWR',
            )
        )

        splash.append(
            label.Label(
                terminalio.FONT,
                text='M=' + str(int(gc.mem_free() / 1024)),
                color=0xFFFFFF,
                x=65,
                y=0,
                label_direction='DWR',
            )
        )
        gc.collect()

    def updateOLED(self, sandbox):
        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(sandbox.active_layers[0])
        gc.collect()

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, board):
        displayio.release_displays()
        i2c = busio.I2C(board.SCL, board.SDA)
        self._display = adafruit_displayio_ssd1306.SSD1306(
            displayio.I2CDisplay(i2c, device_address=0x3C),
            width=self._width,
            height=self._height,
            rotation=self.rotation,
        )
        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(0)

        return

    def before_matrix_scan(self, sandbox):
        if sandbox.active_layers[0] != self._prevLayers:
            self._prevLayers = sandbox.active_layers[0]
            self.updateOLED(sandbox)
        elif self._capsword._cw_active != self._cw_active:
            self._cw_active = self._capsword._cw_active
            self.updateOLED(sandbox)
        return

    def after_matrix_scan(self, sandbox):

        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
