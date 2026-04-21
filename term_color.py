#!/usr/bin/env python

import sys
import argparse
from random import randint

class TermColor:
  def __init__(self, argv=[]):
    self.options = self.get_options(argv)

  def main(self):

    min_c1 = 0
    max_c1 = 96

    if (self.options.favour != None):
      min_c1 = 48

    if (self.options.favour == "grey"):
      i = randint(20, 60)
      c = [i, i, i]
    elif (self.options.favour == "magenta" or
          self.options.favour == "cyan"):
      c = self.get_averaged_color(min_c1, max_c1)
    else:
      c = self.get_color(min_c1, max_c1)

    if (self.options.favour == "red"):
      self.print_color(c[0],c[1],c[2])
    elif (self.options.favour == "green"):
      self.print_color(c[1],c[0],c[2])
    elif (self.options.favour == "blue"):
      self.print_color(c[1],c[2],c[0])
    elif (self.options.favour == "magenta"):
      self.print_color(c[0],c[2],c[1])
    elif (self.options.favour == "cyan"):
      self.print_color(c[2],c[0],c[1])
    else:
      o = self.rand_order()
      self.print_color(c[o[0]],c[o[1]],c[o[2]])

  def get_options(self, argv=[]):
    parser = argparse.ArgumentParser(description='Dark colors for xterms.')
    parser.add_argument('--favour', choices=["red", "green", "blue",
                                             "cyan", "magenta", "grey"])
    parser.add_argument('--xterm', action='store_true')
    parser.add_argument('--xfce4', action='store_true')

    return parser.parse_args(argv)

  def get_color(self, mn, mx):
    # c1 is highest, then c2, then c3
    c1 = randint(mn, mx)
    mx = mx - c1

    c2 = randint(0, mx)
    c3 = mx - c2

    return (c1, c2, c3)

  def get_averaged_color(self, mn, mx):
    # Average the highest two coords (the first two)
    c = self.get_color(mn, mx)
    ave = (c[0] + c[1]) // 2
    return (ave, ave, c[2])

  def rand_order(self):
    orders = ( (0, 1, 2),
               (0, 2, 1),
               (2, 0, 1),
               (2, 1, 0),
               (1, 0, 2),
               (1, 2, 0) )

    o = randint(0, 5)
    return orders[o]

  def print_color(self, r, g, b):
    if self.options.xfce4:
      print("#%02x%02x%02x" % (r, g, b))
    else:
      print("rgb:%02x/%02x/%02x" % (r, g, b))

if __name__ == '__main__':
  TermColor(sys.argv[1:]).main()
