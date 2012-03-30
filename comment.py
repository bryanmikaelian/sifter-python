class Comment(object):
    """Representation of an Issue in Sifter"""
    def __init__(self, issue):
        self.category = issue['category']
        self.body = issue['body']
        self.priority = issue['priority']
        self.commenter = issue['commenter']
        self.milestone_name = issue['milestone_name']
        self.assignee_name = issue['assignee_name']
        self.status = issue['status']
        self.created_at = issue['created_at']
        self.updated_at = issue['updated_at']