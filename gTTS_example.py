# Python3.7.3
# Text to audio example using the gTTS library.
"""Run the program & then open the audio file in your default music
player app & press play."""

import os
from gtts import gTTS

Text = """The Robustness Principle (Postel's Law) Be conservative in what you do,
        be liberal in what you accept from others. Often applied in server
        application development, this principle states that what you send to
        others should be as minimal and conformant as possible, but you should be
        aim to allow nonconformant input if it can be processed. The goal of
        this principle is to build systems which are robust, as they can handle
        poorly formed input if the intent can still be understood. However,
        there are potentially security implications of accepting malformed
        input, particularly if the processing of such input is not well tested."""

print("Please wait...processing")
TTS = gTTS(text=Text, lang='en-uk')

TTS.save("robustnessprinciple.mp3")

os.system("start robustnessprinciple.mp3")
