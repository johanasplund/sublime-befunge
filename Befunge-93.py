#!/usr/bin/python
from __future__ import print_function
import re
import random
import sys
from math import floor


class Field(object):
	def __init__(self, code):
		super(Field, self).__init__()
		self.Y = len(code)
		self.X = max([len(code[l]) for l in range(self.Y)])
		self.code = []
		for c in code:
			if self.X > len(c):
				c += " "*(self.X-len(c))
			self.code.append(list(c))
		self.direction = (1, 0)
		self.xy = (0, 0)
		self.read = False

	def step(self):
		self.xy = ((self.xy[0] + self.direction[0]) % self.X,
					(self.xy[1] + self.direction[1]) % self.Y)

	def change_direction(self, newdir):
		if newdir == "up":
			self.direction = (0, -1)
		elif newdir == "down":
			self.direction = (0, 1)
		elif newdir == "left":
			self.direction = (-1, 0)
		elif newdir == "right":
			self.direction = (1, 0)
		else:
			print("Invalid direction input")

	def stop(self):
		self.direction = (0, 0)

	def print_field(self, font):
		for c in self.code:
			print("".join(c))

	def current_char(self):
		return self.code[self.xy[1] % self.Y][self.xy[0] % self.X]

	def read_unichr(self, textmode):
		self.read = textmode

	def get_char(self, xget, yget):
		return self.code[yget % self.Y][xget % self.X]

	def put_char(self, yput, xput, v):
		self.code[yput % self.Y][xput % self.X] = chr(v)


def pop(stack):
	return 0 if not stack else stack.pop()


def run_code():
	global the_field
	global stack
	global ops
	stack = []
	with open(sys.argv[1], "r") as c:
		codelist = c.read().splitlines()
	the_field = Field(codelist)
	ops = {"+": lambda x1, x2: stack.append(x1 + x2),
			"-": lambda x1, x2: stack.append(x2 - x1),
			"*": lambda x1, x2: stack.append(x1 * x2),
			"/": lambda x1, x2: stack.append(floor(float(x2)/float(x1))),
			"%": lambda x1, x2: stack.append(x2 % x1),
			"`": lambda x1, x2: stack.append(1) if x2 > x1 else stack.append(0),
			"\\": lambda x1, x2: stack.extend([x1, x2]),
			"g": lambda x1, x2: stack.append(ord(the_field.get_char(x2, x1)))}
	instring = ""
	while True:
		if not the_field.read:
			if the_field.current_char() == ">":
				the_field.change_direction("right")
			elif the_field.current_char() == "v":
				the_field.change_direction("down")
			elif the_field.current_char() == "<":
				the_field.change_direction("left")
			elif the_field.current_char() == "^":
				the_field.change_direction("up")
			elif the_field.current_char() == "?":
				the_field.change_direction(random.choice(["right", "down", "up", "left"]))
			elif the_field.current_char() == "@":
				the_field.stop()
				break
			elif re.match("[0-9]", the_field.current_char()):
				stack.append(int(the_field.current_char()))
			elif the_field.current_char() in ops:
				ops[the_field.current_char()](pop(stack), pop(stack))
			elif the_field.current_char() == "!":
				stack.append(1 if pop(stack) == 0 else 0)
			elif the_field.current_char() == "$":
				pop(stack)
			elif the_field.current_char() == "_":
				the_field.change_direction("right") if pop(stack) == 0 else the_field.change_direction("left")
			elif the_field.current_char() == "|":
				the_field.change_direction("down") if pop(stack) == 0 else the_field.change_direction("up")
			elif the_field.current_char() == ".":
				outint = str(pop(stack))
				try:
					print(repr(outint).replace("'", ""), end="")
				except Exception:
					print(ascii(outint).replace("'", ""), end="")
			elif the_field.current_char() == ",":
				outtext = chr(pop(stack))
				try:
					print(repr(outtext).replace("'", "").replace("\\n", "\n").replace("\\t", "\t"), end="")
				except Exception:
					print(ascii(outtext).replace("'", "").replace("\\n", "\n").replace("\\t", "\t"), end="")
			elif the_field.current_char() == ":":
				stack.extend([pop(stack)]*2)
			elif the_field.current_char() == "#":
				the_field.step()
			elif the_field.current_char() == "\"":
				the_field.read_unichr(True)
			elif the_field.current_char() == "p":
				the_field.put_char(pop(stack), pop(stack), pop(stack))
			elif the_field.current_char() == "&":
				stack.append(int(input("Put a number in the stack: ")))
			elif the_field.current_char() == "~":
				if not instring:
					instring = list(input("Put a string in the stack: "))
					instring.append(-1)
					instring = instring[::-1]
					stack.append(ord(instring.pop()))
				else:
					if instring[len(instring)-1] == -1:
						stack.append(int(instring.pop()))
					else:
						stack.append(ord(instring.pop()))
		elif the_field.current_char() == "\"":
			the_field.read_unichr(False)
		else:
			stack.append(ord(the_field.current_char()))
		the_field.step()
	print()
run_code()
