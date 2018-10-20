# UTEchoes
A tool for converting signed raw transactions into Morse code and broadcasting them over FM radio from a Pi Zero.

**Note that, in many jurisdictions, it's illegal to broadcast over FM radio. This is just a proof-of-concept, I'm not advocating its use.**

This uses an exploit with the Raspberry Pi Zero's GPIO pins as detailed [here](http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter).

You'll want to cut a piece of wire (20cm of 14 AWG works well for me), strip the end, and insert it into the fourth GPIO pin down from the SD card slot (the inner column).

Due to the amount of time required to encode a full transaction on the Pi (I just finished one that took 50 minutes, whereas my laptop does it in under 4), it's recommended that 'Morse.py' is run on a higher-spec device and ported over to the Raspberry Pi via SSH or SD card.

The second requires the PiFm module, which you can install from [here](http://omattos.com/pifm.tar.gz). On the Pi, download it using:

`wget -P /home/pi/[WHATEVER DIRECTORY YOU CHOOSE] "http://omattos.com/pifm.tar.gz"`

`tar xf pifm.tar.gz`

Save UTEchoes.py in the same directory to make sure you can use the PiFm module you just downloaded.

Inspired by [Pirate Radio Throwies](https://makezine.com/projects/pirate-radio-throwies/) and [Mule Tools](mule.tools).


### Future Improvements

- Implementing ciphers in case of snooping.

- Testing the range – as far as I know, a ~20cm wire should give you a range of about 100m. I've not explored the limitations myself yet.

- Creating a program to decode the transmission and put it back into readable format, so that it can be broadcast to the network.

- At present, there's a 'bleed' into other FM frequencies (not very desirable, and a possible nuisance – as I mentioned, there are heavy fines in some places for interfering). [This](https://www.youtube.com/watch?v=CuxNGWcftc8&feature=youtu.be) bandpass filter seems to be a way to reduce that.

As always, please feel free to build on top of this. 
