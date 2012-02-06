import urllib2
import json
import issue
import milestone
import category
import user

class Project(object):
	"""Representation of a project in Sifter"""
	def __init__(self, project, token):
		self.api_token = token
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
		issues = []
		url = self.api_issues_url
		req = urllib2.Request(url)
		req.add_header('X-Sifter-Token', self.api_token)
		req.add_header('Accept', 'application/json')
		# Get page one
		json_raw = json.loads(urllib2.urlopen(req).read())
		
		# Set the next page
		next_page = json_raw['next_page_url']
		
		# Set the number of pages
		number_of_pages = json_raw['total_pages']
		
		for	current_page in range(number_of_pages):
			# Create a wrapper for each issue, add it to the list
			raw_issues = json_raw['issues']
			for raw_issue in raw_issues:
				i = issue.Issue(raw_issue)
				issues.append(i)
			
			# Make a request for the next page
			url = next_page
			req = urllib2.Request(url)
			req.add_header('X-Sifter-Token', self.api_token)
			req.add_header('Accept', 'application/json')
			# store the results
			json_raw = json.loads(urllib2.urlopen(req).read())
			
			# set the next page
			if not json_raw['next_page_url']:
				next_page = json_raw['next_page_url']
		
		return issues
	
	def milestones(self):
		"""Gets all the milestones for a given project"""
		milestones = []
		url = self.api_milestones_url
		req = urllib2.Request(url)
		req.add_header('X-Sifter-Token', self.api_token)
		req.add_header('Accept', 'application/json')
		json_raw = json.loads(urllib2.urlopen(req).read())
		
		raw_milestones = json_raw['milestones']
		for raw_milestone in raw_milestones:
			m = milestone.Milestone(raw_milestone)
			milestones.append(m)
			
		return milestones

	def categories(self):
			"""Gets all the categories for a given project"""
			categories = []
			url = self.api_categories_url
			req = urllib2.Request(url)
			req.add_header('X-Sifter-Token', self.api_token)
			req.add_header('Accept', 'application/json')
			json_raw = json.loads(urllib2.urlopen(req).read())
			
			raw_categories = json_raw['categories']
			for raw_category in raw_categories:
				c = category.Category(raw_category)
				categories.append(c)
				
			return categories
	
	def people(self):
			"""Gets all the people for a given project"""
			people = []
			url = self.api_people_url
			req = urllib2.Request(url)
			req.add_header('X-Sifter-Token', self.api_token)
			req.add_header('Accept', 'application/json')
			json_raw = json.loads(urllib2.urlopen(req).read())
			
			raw_people = json_raw['people']
			for raw_user in raw_people:
				u = user.User(raw_user)
				people.append(u)
				
			return people	
