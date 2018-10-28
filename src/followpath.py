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
    r = 0.3
    waittime = 0.4
    # init

    currentPos = drone.pos
    currentWaypointIdx = 0
    nextWaypointIdx = 0
    drone.update()
    for pt in waypoints:
        duration = drone.goToPoint(pt)
        wait(duration + waittime)
        # drone.update()
    drone.update()

    #initial goto
#   duration = drone.goToPoint(waypoints[nextWaypointIdx])
#  starttime=time.time()
#    endtime = starttime+duration+1
#    print("length {0}".format(len(waypoints)))
#    while(nextWaypointIdx<len(waypoints)):
#        drone.update()
#        duration = drone.goToPoint(waypoints[nextWaypointIdx])
#        starttime=time.time()
#        endtime = starttime+duration
#        currentPos = drone.pos
    #     wait(waittime)
    #     print("currentPos",currentPos)
    #     print("waypoint",waypoints[currentWaypointIdx])
    #     if(time.time()>endtime ): #and np.linalg.norm(currentPos-waypoints[currentWaypointIdx])<r
    #         print("accessing {0}".format(currentWaypointIdx))
    #         drone.update()
    #         duration = drone.goToPoint(waypoints[nextWaypointIdx])
    #         print("index ok")
    #         starttime=time.time()
    #         endtime = starttime+duration
    #         currentWaypointIdx+=1
    #         nextWaypointIdx+=1
    # drone.update()
    




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
    nextWaypointIdx = 0

    #initial goto
    duration = drone.goToPoint(waypoints[nextWaypointIdx])
    nextWaypointIdx+=1
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
    
    




		
