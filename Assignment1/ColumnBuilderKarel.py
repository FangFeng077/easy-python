from CollectNewspaperKarel import *
from karel.stanfordkarel import *

"""
File: ColumnBuilderKarel.py
--------------------------------
At present, the ColumnBuilderKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to inspect the two street corners in front of 
its starting position, and build a column (a vertical structure
that is 3 beepers tall) in each avenue that has been marked 
with a beeper, as described in the Assignment 1 handour. Karel 
should end on the 4th avenue, facing east. 
"""


def build_column():
	turn_left()
	move()
	i = 0
	while i < 2:
		put_beeper()
		move()
		i = i + 1

	turn_around()
	move_to_wall()
	turn_left()


def main():
	"""
	You should write your code to make Karel do its task in
	this function. Make sure to delete the 'pass' line before
	starting to write your own code. You should also delete this
	comment and replace it with a better, more descriptive one.
	"""
	i = 0
	while i < 3:
		i += 1
		move()
		if on_beeper():
			build_column()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)