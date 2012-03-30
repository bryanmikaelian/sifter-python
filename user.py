class User(object):
    """Representation of a User in Sifter"""
    def __init__(self, user):
        self.username = user['username']
        self.first_name = user['first_name']
        self.last_name = user['last_name']
        self.email = user['email']
        self.issues_url = user['issues_url']
        self.api_issues_url = user['api_issues_url']