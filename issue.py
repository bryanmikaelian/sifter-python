class Issue(object):
	"""Representation of an Issue in Sifter"""
	def __init__(self, issue):
		self.number = issue['number']
		self.subject = issue['description']
		self.priority = issue['priority']
		self.status = issue['status']
		self.assignee_name = issue['assignee_name']
		self.category_name = issue['category_name']
		self.milestone_name = issue['milestone_name']
		self.opener_name = issue['opener_name']
		self.url = issue['url']
		self.api_url = issue['api_url']
	
