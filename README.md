MPK M2-editor
=============
Alternative to the official AKAI MPKMini MkII Editor

> MPK M2-editor

> Copyright (C) 2017 Damien Picard dam.pic AT free.fr

> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.

> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
> GNU General Public License for more details.

> You should have received a copy of the GNU General Public License
> along with this program. If not, see <http://www.gnu.org/licenses/>.

## Overview
This programme is a replacement for the official Akai MPK Mini MkII Editor. It lacks a few features, but hopefully it will be at least as easy to use as the original.

## Requirements
The programme is written in Python3 and relies on PyQt5 and python-rtmidi. It was tested on GNU/Linux and Windows.

## Installation
A good way would be to use pip for the dependencies.
### Debian-based distributions
```
  apt-get install build-essential python3-dev python3-pip libasound2-dev libjack-dev
  pip3 install python-rtmidi PyQt5
```
### Windows
* Download and install `python3` from [the python website](https://www.python.org/downloads/windows/). Make sure you install `pip` as well in the installer wizard
* Download and install [Visual C++ build tools 2015](http://landinghub.visualstudio.com/visual-cpp-build-tools)
* In a command prompt, type:
```
  pip3 install python-rtmidi PyQt5
```

## Usage
Connect your controller, then start the editor with ```./mpk_m2-editor.py```
If you're familiar with the official editor, you should find it's similar, except that programmes are grouped in tabs at the top of the window. You can send an individual programme or all of them at once. Some fields have tooltips, don't hesitate to hover them.

The Send RAM button allows the editor to send arpeggiator settings.

## Feedback and pull requests welcome!
This is a good starting point. If you would like to contribute, please do so!
