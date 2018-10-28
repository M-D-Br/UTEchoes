import math
import wave
import struct




def append_silence(duration_milliseconds=500):
    num_samples = duration_milliseconds * (sample_rate / 1000.0)
    for x in range(int(num_samples)): 
        audio.append(0.0)
    return


def append_dash(freq=440.0, duration_milliseconds=500, volume=1.0):
    global audio
    num_samples = duration_milliseconds * (sample_rate / 1000.0)
    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))
    return

def append_dot(freq=440.0, duration_milliseconds=200, volume=1.0):
    global audio
    num_samples = duration_milliseconds * (sample_rate / 1000.0)
    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))
    return


def save_wav(file_name):
    wav_file=wave.open(file_name,"w")
    nchannels = 1
    sampwidth = 2
    nframes = len(morsed_list_join)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))
    wav_file.close()
    return



morse = {'a': '.-', 'b': '-...',   'c': '-.-.', 'd': '-..',    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',  '8': '---..', '9': '----.', '0': '-----'}


print('This program will take an input and convert it into Morse code, store it in an audio file, and subsequently broadcast it over FM Radio.')

while True:
  tx_input = raw_input('Please enter your signed transaction:\n')
  tx_input = tx_input.lower()
  confirm = raw_input('Confirm that the input is "' + tx_input + '"?[y/n]')

  if confirm == 'y':
   break

tx_input = str("bgn" + tx_input + "end")
list_input = list(tx_input)
morsed_list = list()



for i in list_input:
  morsed_list.append(morse[i])


morsed_list_join = list(" ".join(morsed_list))

audio = []
sample_rate = 11000.0
print('Working...')
for i in morsed_list_join:
    if i == '.':
        append_dot()
        append_silence(duration_milliseconds=100)
    elif i == '-':
        append_dash()
        append_silence(duration_milliseconds=100)
    else:
        append_silence()
    

save_wav("broadcast.wav")
print('Successfully saved your transmission!')







