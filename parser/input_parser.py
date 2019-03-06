import re, datetime
from filters import Filter
from events import Event

class InputParser(object):

    @staticmethod
    def parse(input):
        """
        Trying to parse input. Depending on it
        will return Filter or Event
        :param input:
        :return:
        """
        input = str(input)
        try:
            message, category, to = re.findall('^(.*)\s#(\S*)\s@(\S*)$', input)[0]
            return Event(message, category, to, datetime.datetime.now())
        except IndexError:
            pass

        try:
            return Filter.create(input)
        except ValueError as e:
            raise ValueError("Input is not valid: \n{}".format(str(e)))