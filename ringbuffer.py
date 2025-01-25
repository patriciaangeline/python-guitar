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

class RingBuffer:
    def __init__(self, capacity: int): # Constructor that creates an empty ring buffer using a circular queue and its necessary variables such as _front, _rear, and sizeQueue
        self.MAX_CAP = capacity
        self._front = 0 
        self._rear = 0
        self.sizeQueue = 0 

        self.buffer = [None]*self.MAX_CAP

    def size(self) -> int: # size() returns the current value of sizeQueue 
        return self.sizeQueue

    def is_empty(self) -> bool: # Returns True if sizeQueue has a value of 0. Otherwise, it returns False 
        if self.size() == 0: 
            return True 
        else: 
            return False 
       
    def is_full(self) -> bool: # Returns True if sizeQueue is equal to self.MAX_CAP. Otherwise, it returns False
        if self.size() == self.MAX_CAP:
            return True
        else: 
            return False

    def enqueue(self, x: float): # Takes in the value x and places it at the last index of the ring buffer if sizeQueue is not full. Otherwise, the RingBufferFull exception is raised
        if self.is_full():
            raise RingBufferFull("Can not enqueue() into a full buffer")
        else:
            self.buffer[self._rear] = x 
            self._rear = (self._rear+1)%self.MAX_CAP
            self.sizeQueue += 1 
     
    def dequeue(self) -> float: # Stores and returns the value of the frontmost index of the ring buffer in a temporary variable so that the value of the frontmost index becomes empty
        if self.is_empty():
            raise RingBufferEmpty("Can not dequeue() from an empty buffer")
        else: 
            self.temp = self.buffer[self._front]
            self.buffer[self._front] = None
            self._front = (self._front+1)%self.MAX_CAP
            self.sizeQueue -= 1
        
        return self.temp

    def peek(self) -> float: # Returns the value of the frontmost index where _front points to. 
        if self.is_empty():
            raise RingBufferEmpty("Can not peek() from an empty buffer")
        else:
            return self.buffer[self._front]


class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
