import sys
sys.path.append("../src")

from followpath import followWaypoints
from drone import Drone
import globals
import api
from path_planning import generateWaypoints
import numpy
import time
import multiprocessing

api.debugMode = True

def sendDrone(droneNum):
	askUser = False
	keepDelivering = True
	droneID = globals.DRONES[droneNum]
	drone = Drone(droneID, globals.DRONEADDRS[droneID])
	try:
		while keepDelivering:
			package = api.package(globals.SWARMNAME)
			drone.getPackage(package)
			drone.currentDelivery = package["id"]
			time.sleep(drone.takeoff(0.3))
			waypoints = generateWaypoints(drone.pos, numpy.array([package["coordinates"][0], package["coordinates"][1], 0.3]))[1:]
			followWaypoints(drone, waypoints)
			time.sleep(drone.land(0))
			drone.deliver()
			time.sleep(drone.takeoff(0.3))
			waypoints = generateWaypoints(drone.pos, drone.home)
			followWaypoints(drone, waypoints)
			time.sleep(drone.land(0))
			if askUser and input("Continue? [y/N]: ") != "y":
				keepDelivering = False
	except Exception as e:
		print(e)
	finally:
		api.stopDrone(globals.SWARMNAME, drone.droneID)
		drone.disconnect()

count = int(input("How many drones? "))
nums = [int(input("Enter drone number: ")) - 24 for i in range(count)]
for drone in nums:
	p = multiprocessing.Process(target=sendDrone, args=(drone,))
	p.start()
	time.sleep(5)
