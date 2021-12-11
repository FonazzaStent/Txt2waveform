# Txt2waveform
The program will convert a text to a waveform and save it into a sound file in WAV format (11025Hz, 8bit). If you use a single word or a very short text, the waveform can be loaded into a synthesizer oscillator, such as the 3xOsc bundled with all versions of FL Studio from Image Line. Envelopes, Filters and other effects can be applied to create a playable instrument. You can turn your name, your city name, your pet's name or your favorite team's name into a synthesizer sound. Longer texts will result in a longer soundfile resembling digital white noise.
The Python script requires Python installed on your system to work. Download the latest version at www.python.org. You also need to install the Pydub library and the FFMPEG codecs through the following commands inside a command line shell such as Windows Command Prompt or PowerShell (hotkey+R and enter "CMD" or "Powershell"):

pip install pydub
pip install python-ffmpeg or pip install ffmpeg

Download FFMPEG from https://www.ffmpeg.org/download.html and install it.
After you installed FFMPEG, you must add it to your PATH environment variable:

Go to Settings, About, Advanced System Settings, Environment Variables, System Variables
Click on "Path", Edit, New
Copy path of folder where you installed FFMPEG, paste to the "path" textfield. Click OK.

If you don't want to install Python, you can just run the executable file included in the package. The text must be contained in a file named text.txt and placed in the same folder as the program, or the program will crash. The program only understands lowercase and capital letters. Spaces and all other punctuation signs, numbers and all non-letter characters will be ignored. After you input your word and press Enter, the program will save the waveform to a file called waveform.wav and close itself. You can now open your synth and import the file as a waveform into the oscillator.
The package contains a file with the waveform corresponding the the word "Hello".
I've also included in this repository the first version of the program (Txt2waveform_old.zip), which does not require Pydub and FFMPEG.
