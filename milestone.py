class Milestone(object):
	"""Representation of a Milestone in Sifter"""
	def __init__(self, milestone):
		self.name = milestone['name']
		self.due_date = milestone['due_date']
		self.issues_url = milestone['issues_url']
		self.api_issues_url = milestone['api_issues_url']
	
