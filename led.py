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
    self.columns = columns
    self.letter_index = 1
    self.letters = {}
    self.letters["i"] = [[1],[1],[1],[1]]
    self.letters["a"] = [[1,1,1,],[1,0,1,],[1,1,1,],[1,0,1,]]
  def write_letter(self,letter: str):
    for idi, i in enumerate(self.letters[letter]):
      for idj, j in enumerate(i):
        self.rows[idi][idj + (self.letter_index)] = (j*255,0,0)
      self.rows[idi].write()

    self.letter_index += len(self.letters[letter][0]) + 1

  def write_string(self,s: str):
    for letter in s:
      self.write_letter(letter)

  def clear(self):
    for i in range(0,len(self.rows)):
      for j in range(0,self.columns):
        self.rows[i][j] = (0,0,0)
      self.rows[i].write()
    self.letter_index = 1

def main():
  m = matrix([Pin(13),Pin(12),Pin(14),Pin(27)],10)
  m.write_string("ia")
  sleep(1)
  m.clear()
  m.write_string("ai")
if __name__ == "__main__":
  main()
