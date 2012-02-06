class Milestone(object):
	"""Representation of a Milestone in Sifter"""
	def __init__(self, milestone):
		self.name = milestone['name']
		self.due_date = milestone['due_date']
		self.issue_url = milestone['issue_url']
		self.api_issue_url = milestone['api_issue_url']
	
