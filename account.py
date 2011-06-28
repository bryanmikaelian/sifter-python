import urllib2

class Account(object):
	"""Account wrapper for Sifter"""
	def __init__(self, host, token):
		self.host = host
		self.token = token
	
	def projects(self):
		"""Gets all the projects from sifter"""
		pass
	
