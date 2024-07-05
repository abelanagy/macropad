print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()

keyboard = KMKKeyboard()
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP2, board.GP3)
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP]
]

encoder_handler.pins = (
    (board.GP17, board.GP16, None,),)

encoder_handler.map = [ (( KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP,),),]

if __name__ == '__main__':
    keyboard.go()
