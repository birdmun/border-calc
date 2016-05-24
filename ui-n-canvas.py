#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ui-n-canvas.py
#  
#  Copyright 2016 Kyle <birdmun@birdmun-Dell-DM051>
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
import ttk as ttk

def user_input(top):
	user_output = tk.Canvas(top, width = 600, height = 600, bg = "white")
	user_output.pack(side = "right")
	firstlbl = tk.Label(top, text = "Size of square")
	firstlbl.pack(side = "left", anchor = tk.N)
	#side_length = tk.StringVar()
	sqsize = tk.Entry(top)
	sqsize.insert(0, 0)
	sqsize.pack(expand = True, anchor = tk.N)
	displaybtn = tk.Button(top, text = "Display", command = matte(user_output, int(sqsize.get())))
	displaybtn.pack()#fill = tk.BOTH, expand = True, anchor = tk.N)

def matte(user_output, side_length):
	user_output.create_rectangle(300 - side_length, 300 - side_length, 300 + side_length, 300 + side_length)

def main():
	top = tk.Tk()
	user_input(top)
	top.update()
	top.mainloop()
	return 0

if __name__ == '__main__':
	main()
