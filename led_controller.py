from machine import Pin
from neopixel import NeoPixel
from time import sleep

class Matrix():
    def __init__(self,pins: list,columns: int):
        self.rows = []
        self.row_count = len(pins)
        self.text = False
        for i in range(0, len(pins)):
            self.rows.append(NeoPixel(pins[i],columns))
        self.columns = columns
        self.letter_index = 0
        self.letters = {
                   'A': [[0,1,0],[1,0,1],[1,1,1],[1,0,1],[1,0,1]],
                   'B': [[1,1,0],[1,0,1],[1,1,0],[1,0,1],[1,1,0]],
                   'C': [[0,1,1],[1,0,0],[1,0,0],[1,0,0],[0,1,1]],
                   'D': [[1,1,0],[1,0,1],[1,0,1],[1,0,1],[1,1,0]],
                   'E': [[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,1,1]],
                   'F': [[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,0,0]],
                   'G': [[0,1,1],[1,0,0],[1,0,1],[1,0,1],[0,1,1]],
                   'H': [[1,0,1],[1,0,1],[1,1,1],[1,0,1],[1,0,1]],
                   'I': [[1,1,1],[0,1,0],[0,1,0],[0,1,0],[1,1,1]],
                   'J': [[0,0,1],[0,0,1],[0,0,1],[1,0,1],[1,1,1]],
                   'K': [[1,0,1],[1,0,1],[1,1,0],[1,0,1],[1,0,1]],
                   'L': [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
                   'M': [[1,0,1],[1,1,1],[1,0,1],[1,0,1],[1,0,1]],
                   'N': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1]],
                   'O': [[0,1,0],[1,0,1],[1,0,1],[1,0,1],[0,1,0]],
                   'P': [[1,1,1],[1,0,1],[1,1,1],[1,0,0],[1,0,0]],
                   'Q': [[1,1,1],[1,0,1],[1,0,1],[1,1,1],[0,0,1]],
                   'R': [[1,1,0],[1,0,1],[1,1,0],[1,0,1],[1,0,1]],
                   'S': [[0,1,1],[1,0,0],[0,1,0],[0,0,1],[1,1,0]],
                   'T': [[1,1,1],[0,1,0],[0,1,0],[0,1,0],[0,1,0]],
                   'U': [[1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]],
                   'V': [[1,0,1],[1,0,1],[1,0,1],[1,0,1],[0,1,0]],
                   'V': [[1,0,1],[1,0,1],[1,0,1],[1,0,1],[0,1,0]],
                   'W': [[1,0,1],[1,0,1],[1,0,1],[1,1,1],[1,0,1]],
                   'X': [[1,0,1],[1,0,1],[0,1,0],[1,0,1],[1,0,1]],
                   'Y': [[1,0,1],[1,0,1],[1,1,1],[0,1,0],[0,1,0]],
                   'Z': [[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,1,1]],
                   ' ': [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
                   }
    def _shift(self,seq, n):
        n = n % len(seq)
        return seq[n:] + seq[:n]

    def clear(self):
        for i in range(0,len(self.rows)):
            for j in range(0,self.columns):
                self.rows[i][j] = (0,0,0)
            self.rows[i].write()
        self.letter_index = 0

    def generate_text(self,string,buff):
        text = []
        for i in range(0,self.row_count):
            text.append([])
        for letter in string:
            for idi, i in enumerate(self.letters[letter]):
                for idj, j in enumerate(i):
                    text[idi].append(j)
                text[idi].append(0)
        for i in range(0,self.row_count):
            for i in range(0,buff):
                text[i].append(0)
        self.text = text

    def write_text(self):
        if self.text != False: 
            self._output(self.text)
        else: 
            print("No Text defined")
            
    def _output(self,text):
        for idi, i in enumerate(text):
            for idj, j in enumerate(i):
                self.rows[idi][idj] = (j*255,0,0)
                if idj == self.columns-1:
                    break
            self.rows[idi].write()

    def rotate_text(self,interval=1,speed=1):
        text = self.text
        while True:
            self._output(text)
            sleep(speed)
            for i in range(0,self.row_count):
                text[i] = self._shift(text[i],interval)

    def shift_text(self,interval=1):
            for i in range(0,self.row_count):
                self.text[i] = self._shift(self.text[i],interval)
