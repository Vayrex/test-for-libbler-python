from datetime import datetime

class Filter(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    @staticmethod
    def create(input = ''):
        """
        Create filter instance depending on provided input
        :param self:
        :param input:
        :return:
        """
        input = str(input)
        if (input.startswith('@')):
            type = 'category'
            value = input[1:]
        elif (input.startswith('#')):
            type = 'to'
            value = input[1:]
        elif (input.startswith('latest')):
            type = 'latest'
            value = input.replace('latest', '')
            value = int(value)
        else:
            parts = input.split(' ')
            if(len(parts) != 2):
                raise ValueError("Not valid input for time range filter"
                                 )
            type = "date"
            time_from = datetime.strptime(parts[0], '%Y-%m-%d_%H:%M')
            time_to = datetime.strptime(parts[1], '%Y-%m-%d_%H:%M')
            value =[time_from, time_to]

        return Filter(type, value)
