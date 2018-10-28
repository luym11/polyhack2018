import sys
sys.path.append("../src")

from followpath import followWaypoints
from drone import Drone
import globals
import api
from path_planning import generateWaypoints
import numpy
import time
import order

askUser = True
api.debugMode = True
keepDelivering = True

droneNum = int(input("Enter drone number: ")) - 24
droneID = globals.DRONES[droneNum]
drone = Drone(droneID, globals.DRONEADDRS[droneID])
try:
	while keepDelivering:
		order.refillQueue()
		parcels = order.getBestBundle(drone.home)
		for parcel in parcels:
			drone.getPackage(parcel)
		time.sleep(drone.takeoff(0.3))
		waypoints = generateWaypoints(drone.pos, numpy.array([parcels[0]["coordinates"][0], parcels[0]["coordinates"][1], 0.3]))
		followWaypoints(drone, waypoints)
		#time.sleep(drone.goToPoint(numpy.array([3.4, 1.4, 0.3])))
		time.sleep(drone.land(0))
		print(drone.deliver())
		time.sleep(drone.takeoff(0.3))
		waypoints = generateWaypoints(drone.pos, drone.home)
		followWaypoints(drone, waypoints)
		#time.sleep(drone.goToPoint(drone.home))
		time.sleep(drone.land(0))
		if askUser and input("Continue? [y/N]: ") != "y":
			keepDelivering = False
except Exception as e:
	print(e)
finally:
	api.stopDrone(globals.SWARMNAME, drone.droneID)
	drone.disconnect()
