subscribers = dict()


def subscribe(event_type: str, function):
    """ Subscribes new function to event type """
    subscribers.setdefault(event_type, [])
    subscribers[event_type].append(function)


def unsubscribe(event_type: str, function):
    """ Unsubscribes new function to event type """
    if event_type in subscribers:
        subscribers[event_type].remove(function)


def notify(event_type: str, data):
    """ Notify listeners of change """
    if event_type not in subscribers:
        return
    for function in subscribers[event_type]:
        function(data)
