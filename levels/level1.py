import sys
sys.path.append("../src")

from followpath import followWaypoints
from drone import Drone
import globals
import api
from path_planning import generateWaypoints
import numpy
import time
import threading
import multiprocessing


api.debugMode = False
DRONEPOSITIONS = {
    "24" : numpy.array([0,0,0]),
	"25" : numpy.array([0,0,0]),
	"26" : numpy.array([0,0,0])
}
HOLDSTATE = {
 	"24" : False,
	"25" : False,
	"26" : False
}

def sendDrone(droneNum, height):
    global HOLDSTATE
    global DRONEPOSITIONS
    HOLDSTATE = globals.HOLDSTATE
    DRONEPOSITIONS = globals.DRONEPOSITIONS

    droneID = globals.DRONES[droneNum]
    drone = Drone(droneID, globals.DRONEADDRS[droneID])
    if(globals.HOLDSTATE["25"]==False):
        HOLDSTATE["25"]=True
    try:
        while True:
            print(globals.HOLDSTATE)
            print(globals.DRONEPOSITIONS)
            HOLDSTATE = globals.HOLDSTATE
            DRONEPOSITIONS = globals.DRONEPOSITIONS

            package = api.package(globals.SWARMNAME)
            drone.getPackage(package)
            drone.currentDelivery = package["id"]
            time.sleep(drone.takeoff(0.3))
            waypoints = generateWaypoints(drone.pos, numpy.array([package["coordinates"][0], package["coordinates"][1], height]))
            print(waypoints)
            followWaypoints(drone, waypoints)
            time.sleep(drone.land(0))
            drone.deliver()
            time.sleep(drone.takeoff(0.3))
            waypoints = generateWaypoints(drone.pos, drone.home)
            followWaypoints(drone, waypoints)
            time.sleep(drone.land(0))
            globals.HOLDSTATE = HOLDSTATE
            globals.DRONEPOSITIONS = DRONEPOSITIONS
    except Exception as e:
        print(e)
    finally:
        api.stopDrone(globals.SWARMNAME, drone.droneID)
        drone.disconnect()

count = int(input("How many drones? "))
nums = [int(input("Enter drone number: ")) - 24 for i in range(count)]


i = 0
for drone in nums:
    # p = multiprocessing.Process(target=sendDrone, args=(drone, 0.3 + i * 0.2))
	print(i)
	print(globals.HOLDSTATE)
	t1 = threading.Thread(target=sendDrone, args=(drone, 0.3 + i * 0.2))
    # p.start()
	t1.start()
	time.sleep(5)
	i += 1
	
