import requests
import json
import project

class Account(object):
    """Account wrapper for Sifter"""
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.url = 'https://' + self.host + '.sifterapp.com' + '/api/projects'

    def request(self, url):
        """Requets JSON object from Sifter url"""
        req = requests.get(url, headers={'X-Sifter-Token':self.token,
                                         'Accept':'application/json'})
        
        return json.loads(req.content)
            
    def projects(self):
        """Gets all the projects from sifter"""
        projects = []
        json_raw = self.request(self.url)
        raw_projects = json_raw['projects']
        for raw_project in raw_projects:
            proj = project.Project(raw_project, self)
            projects.append(proj)
        
        return projects