#!/usr/bin/env python3

'''
We hereby attest to the truth of the following facts: 

We have not discussed the Python code in our program with anyone 
other than our instructor or the teaching assistants assigned to this course. 

We have not used Python code obtained from another student, or
any other unauthorized source, whether modified or unmodified. 

If any Python code or documentation used in our program was 
obtained from another source, it has been clearly noted with citations in the 
comments of our program
'''

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    stdkeys.create_window()
    # creates the GuitarString objects 
    # which is tied to the index of the chars in keyboard
    # and adds it to list
    keyboard = 'q2we4r5ty7u8i9op-[=]'
    guitarStrings = []
    for h in keyboard:
        ind = keyboard.find(h)
        freq = 440 * (1.059463**(ind-12))
        guitarStrings.append(GuitarString(freq))

    pluckedStrings = set() # Set of all chars that have been typed

    n_iters = 0
    while True:
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            index = keyboard.find(key) # Finds if 'key' is a char in keyboard
            if key == "":
                continue
            elif index != -1: 
                length = len(pluckedStrings)
                if length < 10: # Limits the amount of plucked strings in the set so it won't crash when spammed
                    pluckedStrings.add(guitarStrings[index])
                    guitarStrings[index].pluck()
                else:
                    pluckedStrings.pop()

        sample = 0 
        for s in pluckedStrings.copy(): # Plays the sample of all the plucked strings
            sample += s.sample()
            s.tick()
            if s.time() > 81600: # Removes a plucked string if it can no longer be heard
                pluckedStrings.remove(s)
                s.lastPlucked()

        play_sample(sample)
