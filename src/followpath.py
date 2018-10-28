import time
import globals
import numpy as np

def followWaypoints(waypoints, drone):
    """Commands a drone to follow a set of waypoints

    Args:
        waypoints: A list of waypoints to follow as tuples
        drone: Drone ID

    Returns:
        Something
    """
    r = 0.05
    waittime = 0.01
    # init

    currentPos = drone.pos
    currentWaypointIdx = 0
    nextWaypointIdx = 0

    #initial goto
    duration = drone.goToPoint(waypoints[nextWaypointIdx])
    starttime=time.time()
    endtime = starttime+duration
    print("length {0}".format(len(waypoints)))
    while(nextWaypointIdx<len(waypoints)):
        currentPos = drone.pos
        wait(waittime)
        if(time.time()>endtime):
            print("accessing {0}".format(nextWaypointIdx))
            duration = drone.goToPoint(waypoints[nextWaypointIdx])
            print("index ok")
            starttime=time.time()
            endtime = starttime+duration
            currentWaypointIdx+=1
            nextWaypointIdx+=1
    drone.update()
    




def followWaypointsComplex(waypoints, drone):
    """Commands a drone to follow a set of waypoints

    Args:
        waypoints: A list of waypoints to follow as tuples
        drone: Drone ID

    Returns:
        Something
    """
    r = 0.05
    waittime = 0.01
    # init

    currentPos = drone.pos
    currentWaypointIdx = 0
    nextWaypointIdx = 1

    #initial goto
    duration = drone.goToPoint(waypoints[nextWaypointIdx])

    while(nextWaypointIdx<len(waypoints)-1):
        wait(waittime)
        drone.update()
        currentPos = drone.pos
        currentWaypointIdx_tmp = getCurrentWaypointIdx(currentPos, waypoints,r)
        
        if(currentWaypointIdx_tmp == nextWaypointIdx):
        
            currentWaypointIdx += 1
            nextWaypointIdx += 1
            drone.goToPoint(waypoints[nextWaypointIdx])
            drone.update()
        
#        else:
        
#           currentWaypointIdx = currentWaypointIdx_tmp
#            nextWaypointIdx = currentWaypointIdx+1
#            drone.goToPoint(waypoints[nextWaypointIdx])
#            drone.update()


        


def wait(waitTime):
    """wait a defined time to update the positions

	Args:
		waitTime: seconds to wait
	
	Returns:
		nothing
	"""
    time.sleep(waitTime)


def getCurrentWaypointIdx(pos, waypoints,r):
    """find the Way point it is currently on.

	Args:
		pos: current drone positon
        waypoints: array of np.arrays, the list of waypoints
	
	Returns:
		index of the current waypoint if currently in the range of a waypoint
        -1 if currently not in the range of any waypoint
	"""
    for idx, point in enumerate(reversed(waypoints)):
        idx+=1
        if(inRangeOfWaypoint(pos, point,r)):
            return len(waypoints)-idx
       
    return -1
        



def inRangeOfWaypoint(pos, waypointPos,r):  
    """check if the position is on the waypoint

	Args:
		pos: postion of the drone
        waypointPos: position of the waypoint
	
	Returns:
		true or false if it is in the range of the waypoint
	""" 

    diff = abs(pos-waypointPos)

    return (diff[0]<r and diff[1]<r and diff[2]<r)
    
    




		
