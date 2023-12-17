from event_module import *
from heapq import heappop
from pprint import pformat
from heapq import heappush

class FutureEventList:
    def __init__(self):
        self.events = []

    def __iter__(self):
        return self

    def __next__(self) -> Event:
        if self.events:
            return heappop(self.events)
        raise StopIteration

    def __repr__(self) -> str:
        return pformat(self.events)
    def empty(self):
        return len(self.events) == 0

def schedule(e: Event, fev: FutureEventList):
    heappush(fev.events, e)

E_list =FutureEventList()
