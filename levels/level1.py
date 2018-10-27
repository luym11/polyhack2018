import sys
sys.path.append("../src")

import followpath
import signal
from drone import Drone
import globals
import api
from path_planning import generateWaypoints

keepDelivering = True

def terminate(sig, frame):
	global keepDelivering
	keepDelivering = False

signal.signal(signal.SIGINT, terminate)

droneNum = int(input("Enter drone number: ")) - 24
droneID = globals.DRONES[droneNum]
drone = Drone(droneID, globals.DRONEADDRS[droneID])
while keepDelivering:
	package = api.package(globals.SWARMNAME)
	drone.land(0)
	drone.getPackage(package)
	drone.takeoff(1)
	waypoints = generateWaypoints(drone.pos, numpy.array([package["coordinates"][0], package["coordinates"][1], package["coordinates"][2]]))
	followWaypoints(drone, waypoints)
	drone.land(0)
	drone.deliver()
	drone.takeoff(1)
	waypoints = generateWaypoints(drone.pos, drone.home)
	followWaypoints(drone, waypoints)
drone.disconnect()
