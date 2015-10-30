#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tk-play.py
#  
#  Copyright 2015 suerose <suerose@suerose-OptiPlex-GX280>
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
import ttk
import Tkinter as tk
#import tkMessageBox

def user_input(top):
	int_border_count = 1
	#scrollbar = tk.Scrollbar(top, orient = "vertical")
	ent_border_color = {}
	ent_border_pn = {}
	# User Input Labels
	list_labels_static = ["Customer Order Number", "Picture height", 
		"Picture width", "Frame height", "Frame width", "Number of borders"]
	list_labels_border = ["Border color", "Border part number", "Bevel",
		"Border width"]
	for i in list_labels_static:
		lbl_static_label = tk.Label(top, text = i)
		lbl_static_label.grid(row = list_labels_static.index(i), column = 0, 
			sticky = "E")
	ent_order_number = tk.Entry(top)
	ent_order_number.grid(row = 0, column = 1)
	ent_picture_height = tk.Entry(top)
	ent_picture_height.grid(row = 1, column = 1)
	ent_picture_width = tk.Entry(top)
	ent_picture_width.grid(row = 2, column = 1)
	ent_frame_height = tk.Entry(top)
	ent_frame_height.grid(row = 3, column = 1)
	ent_frame_width = tk.Entry(top)
	ent_frame_width.grid(row = 4, column = 1)
	sb_border_count = tk.Spinbox(top, from_ = 1, to = 3, width = 1)
	sb_border_count.grid(row = 5, column = 1, sticky = "W")
	for i in range(1, int_border_count + 1):
		for j in list_labels_border:
			lbl_border = tk.Label(top, text = j)
			lbl_border.grid(row = list_labels_border.index(j) + (6 * i), 
				column = 0, sticky = "E")
		box_value = tk.StringVar()
		ent_border_color[i] = ttk.Combobox(top, textvariable = box_value,
			width = 18)
		ent_border_color[i, "values"] = ("Red", "Orange", "Yellow", "Blue",
			"Indigo", "Violet", "Gold", "Silver")
		ent_border_color[i].grid(row = (6 * i), column = 1, sticky = "W")
		ent_border_pn[i] = tk.Entry(top)
		ent_border_pn[i].grid(row = (6 * i) + 1, column = 1)
			#~ ent_border[i, list_labels_border.index(j)]  = tk.Entry(top)
			#~ ent_border[i, list_labels_border.index(j)].grid(row =
				#~ list_labels_border.index(j) + (6 * i) + 6, column = 1)
			
	
		

def main():
	top = tk.Tk()
	user_input(top)
	top.mainloop()
	return 0

if __name__ == '__main__':
	main()

