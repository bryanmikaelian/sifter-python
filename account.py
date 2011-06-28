import urllib2
import json
import project

class Account(object):
	"""Account wrapper for Sifter"""
	def __init__(self, host, token):
		self.host = host
		self.token = token
	
	def projects(self):
		"""Gets all the projects from sifter"""
		projects = list()
		url = self.host + '/api/projects'
		req = urllib2.Request(url)
		req.add_header('X-Sifter-Token', self.token)
		json_raw = json.loads(urllib2.urlopen(req).read())
		raw_projects = json_raw['projects']
		for raw_project in raw_projects:
			p = project.Project(raw_project)
			projects.append(p)
		
		return projects
	
