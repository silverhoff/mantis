class Project:

    def __init__(self, name=None, status=None, enabled=None, view_status=None, description=None, id=None):
        self.name = name
        self.status = status
        self.enabled = enabled
        self.view_status = view_status
        self.descriptiom = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.view_status, self.name, self.status, self.enabled, self.descriptiom)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name