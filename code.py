# This is the custom written firmware for my macropad using the kmk library.

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.LED import LED
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap, Delay

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
led = LED(led_pin=[board.GP16]) # The LEDs can indicate bootup and which layer is currently active.
# led = LED(led_pin=[board.GP16, board.GP17, board.GP18]) # The LEDs can indicate bootup and which layer is currently active.
macros = Macros()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2)   # Key matrix consisting of 3 columns and 5 rows.
keyboard.row_pins = (board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(led)
keyboard.modules = [encoder_handler]
keyboard.modules.append(macros)


OPEN_MESSENGER = KC.MACRO(  # These are the macros for opening the respective applications.
    Tap(KC.LGUI),  # The first key is the windows key, which opens the start menu.
    Delay(200),
    "Messenger",   # The second key is the name of the application.
    Delay(200),
    Tap(KC.ENTER), # It then searches for the application in the start menu.
)

OPEN_DC = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "Discord",
    Delay(200),
    Tap(KC.ENTER),
)
OPEN_GG = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "SteelSeries GG",
    Delay(200),
    Tap(KC.ENTER),
)

keyboard.keymap = [
    [   # Base Layer
        KC.NO, KC.LGUI(KC.L), KC.AUDIO_MUTE,   # The first key is a layer switcher, the second key locks the pc and the third key is a mute button. This works together with the rotary encoder functionality.
        OPEN_MESSENGER, OPEN_DC, OPEN_GG,   # These are the macros for opening the respective applications.
        KC.NO, KC.NO, KC.NO,    # These keys are not yet assigned.
        KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO
    ]
]

encoder_handler.pins = (
    (board.GP8, board.GP9, None),   # The third pin could be used for the button of the rotary encoders, but in my case, it is hooked up to the key matrix.
    (board.GP10, board.GP11, None),
    (board.GP12, board.GP13, None)
    )

encoder_handler.map = [
    (  # Base layer
        ( KC.NO, KC.NO, None), # No action for the first encoder yet
        ( KC.BRID, KC.BRIU, None),  # Brightness down and up
        ( KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, None) # Volume down and up
    )
]

if __name__ == '__main__':
    keyboard.go()
