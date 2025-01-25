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

from math import ceil
import random
from ringbuffer import RingBuffer

class GuitarString:
    def __init__(self, frequency: float): # Constructor that creates a guitar string based on a given frequency using a sampling rate of 44100hz
        self.numberTicks = 0
        self.SAMP_RATE = 44100
        self.DECAY = float(0.996) 
        self.frequency = frequency

        self.capacity = ceil(self.SAMP_RATE/self.frequency)
        self.buffer = RingBuffer(self.capacity)
        for x in range(self.capacity):
            self.buffer.enqueue(0)

    @classmethod
    def make_from_array(cls, init: list[int]): # Create a guitar string whose size and initial values are given by the array `init`
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self): # Sets the ring buffer to white noise by randomizing its values from -0.5 to 0.5
        for x in range(self.capacity):
            self.buffer.dequeue()
            self.buffer.enqueue(random.uniform(-0.5, 0.5))


    def tick(self): # Applies the Karplus--Strong formula that enqueues the string 
        self.first = self.buffer.dequeue()
        self.second = self.buffer.peek()
        self.average = self.DECAY*(0.5*(self.first+self.second))
        self.buffer.enqueue(self.average)
        self.numberTicks += 1


    def sample(self) -> float: # Returns the front most value of the string
        return self.buffer.peek()


    def time(self) -> int: # Returns the number of times ticks was called
        return self.numberTicks

    def lastPlucked(self) -> int: # Sets tick counter to 0 when it is replucked
        self.numberTicks = 0
    