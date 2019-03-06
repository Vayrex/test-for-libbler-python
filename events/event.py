class Event(object):

    message = None
    category = None
    to = None
    time = None

    def __init__(self, message, category, to, time):
        self.message = message
        self.category = category
        self.to = to
        self.time = time

    
