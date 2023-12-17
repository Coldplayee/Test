from intersection import *


class Lane:
    def __init__(self, intersection, direction):
        self.intersection = intersection
        self.direction = direction
        self.queue = []
        self.exit_vehicle = 0
    def queue_vehicle(self, vehicle):
        self.queue.append(vehicle)

    def dequeue_vehicle(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None
    def vehicle_increment(self):
        self.exit_vehicle += 1