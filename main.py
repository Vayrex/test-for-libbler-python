from filters import Filter
from events import EventManager
from parser import InputParser



def main():
    value = input('You can type command: \n'
          '@{name} - to get events from provided category. Example: @update\n'
          '#{name} - to get events intended to some recipient. Example: #john\n'
          'latest{N} - to get latest N events\n'
          '------------------------------------------\n')

    try:
        event_or_filter = InputParser.parse(value)
    except Exception as e:
        print(str(e))
        print('----------------------------------')
        return main()

    if(isinstance(event_or_filter, Filter)):
        events = manager.get_by(event_or_filter)
        print('-----------------------------')
        print(events)
        print('-----------------------------')
    else:
        manager.append(event_or_filter)

    return main()




if(__name__ == "__main__"):
    manager = EventManager()
    main()