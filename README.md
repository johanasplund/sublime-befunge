Befunge-93 for Sublime Text
===============

This package provides syntax highlighting and an interpreter for the esoteric programming language Befunge-93 for Sublime Text 2 and 3 written in Python. The syntax highlighting is loosely based on [Pygments](http://pygments.org/). I have not done any extensive testing with Sublime Text 2 so while it should work properly, I can not assure it.

A standalone visual interpreter written in Python and pygame is found at https://github.com/johanasplund/befunge-93.

Befunge-93 is a two-dimensional esoteric programming language in the Funge-family made by Chris Pressey in 1993, which was made as an attempt of creating a language which was as hard as possible to compile. Befunge-93 consists of a two-dimensional *play field* and a *program-counter*. The program-counter begins at a set location (upper-left corner of the play field) and initially travels to the right. As the program-counter travels it encounters instructions, which gets executed.

## How to install

Install via [Package Control](https://sublime.wbond.net/packages/Package%20Control) or download the latest source at [github](https://github.com/johanasplund/sublime-befunge/), and put all files in `Packages/Befunge-93`. The Packages folder is located at
- OSX: `~/Library/Application Support/Sublime Text X/Packages/`
- Linux `~/.config/Sublime Text X/Packages/`
- Windows `%UserProfile%\AppData\Roaming\Sublime Text X\Packages\`

## Todo
- ~~Implement an [interpreter](https://github.com/johanasplund/befunge-93)~~
- Make the output cleaner and without numerous unicode-characters
