#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  canvas-test.py
#  
#  Copyright 2016 suerose <suerose@suerose-OptiPlex-GX280>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import Tkinter as tk

def main():
	animation = tk.Tk()
	canvas_1 = tk.Canvas(animation, height = 400, width = 400, bg = "white")
	canvas_1.pack()
	#order of objects is important. objects are stacked bottom to top from first to last
	canvas_1.create_line(0, 0, 400, 400)
	#canvas_1.create_rectangle(100, 100, 300, 300, outline = "green", fill = "red",
	#	activefill = "purple", width = 5, activedash = (7, 13, 5, 4))
	canvas_1.create_rectangle(100, 100, 300, 300, fill = "red")
	canvas_1.create_rectangle(150, 150, 250, 250, fill = "purple")
	canvas_1.create_text(200, 200, text = "click me", fill = "yellow", font = "bold")
	animation.update()
	animation.mainloop()
	return 0

if __name__ == '__main__':
	main()

