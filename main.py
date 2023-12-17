import heapq
import time
from vehicle import *
from intersection import *
from event_module import *
from future_event_list import *
from state import *
from input import *
from traffic_simulation import *

# global_state = State(
#     total_entered=0,
#     total_departed=0,
#     total_travel_time=0.0,
#     total_departure_time=0,
#     total_events=0
# )

def setup_initial_events(vehicles, intersections, future_event_list, lambda_rate_south_north, lambda_rate_east_west,Timelimit):
    for vehicle in vehicles:
        entry_time = vehicle.entry_time
        entry_intersection = vehicle.entry_intersection
        schedule(simulation_arrival(entry_time, vehicle, intersections, future_event_list), future_event_list)

    for intersection in intersections:
        schedule(trafficlight_change(random.randint(0, 5), intersection, intersections, future_event_list), future_event_list)
    for i in range(0,TimeLimit,30):
        schedule(report_info(i,intersections,future_event_list),future_event_list)


global E_list
TimeLimit = 3600
vehicles = initialize_vehicles(10)
intersections = initialize_intersections(5)
setup_initial_events(vehicles, intersections, E_list, lambda_rate_south_north, lambda_rate_east_west,TimeLimit)
simulate(E_list,TimeLimit)
