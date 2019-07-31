class Project:

    def __init__(self, name, status=None, view_state=None, description=None):
        self.name = name
        self.status = status
        self.view_state = view_state
        self.description = description