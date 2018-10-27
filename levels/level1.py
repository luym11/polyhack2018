import ../src/followPath
import signal
import sys

keepDelivering = True

def terminate():
	global continue
	keepDelivering = False

signal.signal(signal.SIGINT, terminate)

droneNum = input("Enter drone number: ") - 24
drone = Drone(globals.DRONES[droneNum], globals.DRONEADDRS[droneNum])
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
