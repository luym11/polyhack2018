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

def sendDrone(droneNum, trajectories):
	droneID = globals.DRONES[droneNum]
	drone = Drone(droneID, globals.DRONEADDRS[droneID])
	try:
		while True:
			package = api.package(globals.SWARMNAME)
			drone.getPackage(package)
			drone.currentDelivery = package["id"]
			time.sleep(drone.takeoff(0.3))
			print("1")
			waypoints = generateWaypoints(drone.pos, numpy.array([package["coordinates"][0], package["coordinates"][1], 0.3]))
			print(waypoints)
			print("1.5")
			followWaypoints(drone, waypoints, trajectories)
			print("2")
			time.sleep(drone.land(0))
			drone.deliver()
			time.sleep(drone.takeoff(0.3))
			waypoints = generateWaypoints(drone.pos, drone.home)
			followWaypoints(drone, waypoints, trajectories)
			time.sleep(drone.land(0))
	except Exception as e:
		print(e)
	finally:
		api.stopDrone(globals.SWARMNAME, drone.droneID)
		drone.disconnect()

manager = multiprocessing.Manager()
trajectories = manager.dict()

count = int(input("How many drones? "))
nums = [int(input("Enter drone number: ")) - 24 for i in range(count)]
proc = None
for drone in nums:
	trajectories[globals.DRONES[drone]] = {}
	p = multiprocessing.Process(target=sendDrone, args=(drone, trajectories))
	p.start()
	proc = p
	time.sleep(5)
proc.join()
