# About
sifter-python is a simple wrapper for the Sifter API.  It is written in python and is modeled around the work Garrett Dimon and Adam Keys did with their ruby gem.

This is a work in progress (like my C-Sharp wrapper) and will slowly include milestones, issues, and other resources.

# Getting the projects and issues
	import account
	
    a = account.Account(host,token)
    a.projects() # Returns a list of projects
	
	# Get the issues for a project (in this case the first project)
	a.projects()[0].issues()


# Thoughts, comments, suggestions?
Feel free to message me or fork the repo and implement your own solution!