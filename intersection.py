from lane import *

class Intersection:
    def __init__(self, intersection_id, redlight_duration, greenlight_duration, left_duration,distance_to_intersection, distance_to_next_intersection, final_intersection_id):
        self.intersection_id = intersection_id
        self.lanes = {
            'N': Lane(self, 'N'),
            'S': Lane(self, 'S'),
            'E': Lane(self, 'E'),
            'W': Lane(self, 'W'),
            'Nleft': Lane(self, 'Nleft'),
            'Sleft': Lane(self, 'Sleft'),
            'Eleft': Lane(self, 'Eleft'),
            'Wleft': Lane(self, 'Wleft')
        }

        self.lights = {'N': 'green', 'S': 'green', 'E': 'red', 'W': 'red','Nleft': 'red', 'Sleft': 'red', 'Eleft': 'red', 'Wleft': 'red'}
        # self.lights = {'N': 'red', 'S': ['red', 'red'], 'E': ['red', 'red'], 'W': ['red', 'red']}

        self.redlight_duration = redlight_duration  # in seconds
        self.greenlight_duration = greenlight_duration  # in seconds
        self.left_duration  = left_duration 
        self.distance_to_intersection = distance_to_intersection  # in meters
        self.distance_to_next_intersection = distance_to_next_intersection  # in meters
        # self.distance_to_exit = 100  # in meters

        self.next_intersection_id = intersection_id + 1
        if self.next_intersection_id > final_intersection_id:
            self.next_intersection_id = None

        # Use four servers to represent whether a certain direction of the intersection is occupied.
        # False means that direction is not occupied by vehicle.
        self.NorthBound = False
        self.SouthBound = False
        self.EastBound = False
        self.WestBound = False

    def change_lights(self, direction):
        if self.lights[direction] == 'red':
            self.lights[direction] = 'green'
        else:
            self.lights[direction] = 'red'

    def get_intersection_id(self):
        return self.intersection_id

    def get_light_state(self, direction):
        return self.lights[direction]

    def get_redlight_duration(self):
        return self.redlight_duration

    def get_greenlight_duration(self):
        return self.greenlight_duration
    
    def get_left_duration(self):
        return self.left_duration

    def get_distance_to_intersection(self):
        return self.distance_to_intersection

    def get_distance_to_next_intersection(self):
        return self.distance_to_next_intersection

    def get_next_intersection_id(self):
        return self.next_intersection_id

    def get_northbound_state(self):
        return self.NorthBound

    def get_southbound_state(self):
        return self.SouthBound

    def get_eastbound_state(self):
        return self.EastBound

    def get_westbound_state(self):
        return self.WestBound

    def occupy_northbound(self):
        self.NorthBound = True

    def occupy_southbound(self):
        self.SouthBound = True

    def occupy_eastbound(self):
        self.EastBound = True

    def occupy_westbound(self):
        self.WestBound = True
