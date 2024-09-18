from machine import Pin
from neopixel import NeoPixel
from time import sleep

class Matrix():
    def __init__(self,pins: list,columns: int):
        self.rows = []
        self.row_count = len(pins)
        self.text = False
        self.off = (0,0,0)
        for i in range(0, len(pins)):
            self.rows.append(NeoPixel(pins[i],columns))
        self.columns = columns
        self.letter_index = 0
        self.letters = {
                'A': [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]],
                'B': [[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,0]],
                'C': [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1],[0,1,1,1,0]]
                'B': [[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,0]],

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

    def generate_text(self,string,buff,cchannel=()):
        if len(cchannel) != len(string):
            print("Not equal")
            exit()
        text = []
        for i in range(0,self.row_count):
            text.append([])
        for idtext,letter in enumerate(string):
            for idi, i in enumerate(self.letters[letter]):
                for idj, j in enumerate(i):
                    text[idi].append((j*cchannel[idtext][0],j*cchannel[idtext][1],j*cchannel[idtext][2]))
                text[idi].append(self.off)
        for i in range(0,self.row_count):
            for j in range(0,buff):
                text[i].append(self.off)
        self.text = text

    def write_text(self):
        if self.text != False: 
            self._output(self.text)
        else: 
            print("No Text defined")
            
    def _output(self,text):
        for idi, i in enumerate(text):
            for idj, j in enumerate(i):
                self.rows[idi][idj] = j
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


def main():
    m = Matrix([Pin(13),Pin(12),Pin(14),Pin(27),Pin(26),Pin(25),Pin(33)],20)
    m.generate_text("ABCA",5,
    [
        (80,255,255),
        (80,255,255),
        (0,255,0),
        (80,255,0),
    ]
    )
    m.rotate_text(speed=0.5)
if __name__ == "__main__":
    main()

