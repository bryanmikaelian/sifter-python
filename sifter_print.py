#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sifter_print.py
#       
#       Copyright 2012 Mark Mikofski <marko@linuxBox>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       

import account

def main():
	host = input('Enter your sifterapp url in quotes:')
	token = input('Enter your sifter access key in quotes:')
	
	a = account.Account(host,token)
	
	projects = a.projects()
	for p in projects:
		print
		print p.name
		issues = p.issues()
		for i in issues:
			print i.number, i.subject
			end
			
		milestones = p.milestones()
		for m in milestones:
			print m.name, m.due_date
			
	
	return 0

if __name__ == '__main__':
	main()

