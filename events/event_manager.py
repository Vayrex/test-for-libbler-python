from events import Event

class EventManager(object):

    events = []

    def __init__(self, events = []):
        self.events = events

    def append(self, event):
        """
        Add an event to events
        :param event:
        :return:
        """
        if(not isinstance(event, Event)):
            raise TypeError("Expecting for Event instance, but '{}' was provided.".format(event.__class__.__name__));

        self.events.append(event)

    def all(self):
        """
        Return all events
        :return:
        """
        return self.events

    def get_by(self, filter):
        """
        Depending on filter will return events
        :param filter:
        :return:
        """
        filter_type = filter.type
        value = filter.value

        if(filter_type == "category"):
            return self.get_by_category(value)
        elif(filter_type == "to"):
            return  self.get_by_to(value)
        elif(filter_type =="latest"):
            return  self.get_latest(value)
        elif(filter_type =="time"):
            return  self.get_by_date_range(value)
        else:
            raise ValueError("Invalid filter type. "
                             "Expected one of 'category', 'to', 'latest', 'time', "
                             "but got '{}'".format(str(filter_type)))


    def get_latest(self, count):
        """
        Return N latest events
        :param count:
        :return:
        """
        return self.events[-int(count):]

    def get_by_category(self, category):
        """
        Filter events by category
        :param category:
        :return:
        """
        return [event for event in self.events if event.category == str(category)]

    def get_by_to(self, to):
        """
        Filter events by recipient
        :param to:
        :return:
        """
        return [event for event in self.events if event.to == str(to)]

    def get_by_date_range(self, time_from, time_to):
        """
        Return events between 2 time points
        :param time_from:
        :param time_to:
        :return:
        """
        return [event for event in self.events if time_from <= event.time and time_to <= event.date]

