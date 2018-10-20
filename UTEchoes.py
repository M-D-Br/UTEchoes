import time
import PiFm

print('Welcome to UTEchoes!\n')
print('This program will take the broadcast.wav file you created earlier and transmit it over FM radio (at 103.3FM).')

print("Loop 1 in progress...")
PiFm.play_sound("broadcast.wav")
time.sleep(60)
print("Loop 2 in progress...")
PiFm.play_sound("broadcast.wav")
time.sleep(60)
print("Loop 3 in progress...")
PiFm.play_sound("broadcast.wav")
time.sleep(60)
print("Done!")
