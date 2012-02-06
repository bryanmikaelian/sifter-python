#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sifter_print.py
#       
#       Copyright 2012 Mark Mikofski <marko@bwanamaro@yahoo.com>
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
	# ask the user for the host and token
	host = input('Enter your sifterapp url in quotes:')
	token = input('Enter your sifter access key in quotes:')
	# host
	# 	the complete url to your sifter subdomain
	# 	i.e.: "https://mycompany.sifterapp.com"
	# token
	# 	the 32-character hexdex access key from my profile page

	a = account.Account(host,token) # instantiate and account
	
	projects = a.projects() # use projects method to get projects
	
	# dprint some of your project info to the screen to test that
	# sifter-python is working
	for p in projects:
		print
		print p.name # print project name
		# print issues info
		issues = p.issues()
		for i in issues:
			print i.number, i.status, i.priority, i.subject
			
		print
		print "*** milestones ***"
		milestones = p.milestones()
		for m in milestones:
			print m.name, m.due_date

		print
		print "*** categories ***"			
		categories = p.categories()
		for c in categories:
			print c.name
			
		print
		print "*** people ***"			
		people = p.people()
		for u in people:
			print u.first_name,u.last_name
			
		print
		print "****************************************"
	
	return 0

if __name__ == '__main__':
	main()

