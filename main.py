# NeoPixels Rainbow on MicroPython
# Wokwi Example https://wokwi.com/arduino/projects/305569065545499202

from machine import Pin
from neopixel import NeoPixel
from time import sleep



class matrix():
  def __init__(self,pins: list,columns: int):
    self.rows = []
    for i in range(0, len(pins)):
      self.rows.append(NeoPixel(pins[i],columns))
    self.letter_count = 0
    self.letter_width = 3
    self.letters = {}
    self.letters["i"] = [[0,0,0],[0,1,0],[0,1,0],[0,1,0]]

  def write_letter(self,letter):
    for idi, i in enumerate(self.letters[letter]):
      for idj, j in enumerate(i):
        print(idi)
        self.rows[idi][idj + (self.letter_width * self.letter_count)] = (j*255,0,0)
    for i in range(0,len(self.rows)):
      self.rows[i].write()
    self.letter_count +=1

def main():
  m = matrix([Pin(13),Pin(12),Pin(14),Pin(27)],10)
  m.write_letter("i")
  m.write_letter("i")
if __name__ == "__main__":
  main()
