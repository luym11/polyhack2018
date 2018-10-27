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
    pos = drone.pos

    currentPos = drone.home
    currentWaypointIdx = 0
    nextWaypointIdx = 1
    drone.goToPoint(waypoints[nextWaypointIdx])
    while(currentWaypointIdx<len(waypoints)):
        currentPos = drone.pos
        currentWaypointIdx_tmp = getCurrentWaypointIdx(currentPos, waypoints)
        if(currentWaypointIdx_tmp = currentWaypointIdx):
            wait()
            drone.update()
        elif(currentWaypointIdx_tmp = nextWaypointIdx):
            currentWaypointIdx += 1
            nextWaypointIdx += 1
            drone.goToPoint(waypoints[nextWaypointIdx])
            drone.update()
        else:
            currentWaypointIdx = currentWaypointIdx_tmp
            nextWaypointIdx = currentWaypointIdx+1
            drone.goToPoint(waypoints[nextWaypointIdx])
            drone.update()


        


def wait():



def getCurrentWaypointIdx(pos, waypoints):
    for idx, point in enumerate(waypoints):
        idx+=1
        if(inRangeOfWaypoint(pos, point)):
            return idx
       
    return -1
        



def inRangeOfWaypoint(pos, waypointPos):   

    diff = abs(pos-waypointPos)

    return (diff[0]<r and diff[1]<r and diff[2]<r)
    
    




		
