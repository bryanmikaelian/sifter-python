import issue

class Project(object):
	"""Representation of a project in Sifter"""
	def __init__(self, project):
		self.issues_url = project['issues_url']
		self.archived = project['archived']
		self.url = project['url']
		self.milestones_url = project['milestones_url']
		self.api_people_url = project['api_people_url']
		self.api_issues_url = project['api_issues_url']
		self.api_milestones_url = project['api_milestones_url']
		self.api_categories_url = project['api_categories_url']
		self.name = project['name']
	
	def issues(self):
		"""Gets all the issues for a given project"""
		pass
