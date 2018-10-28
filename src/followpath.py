import globals
import time

def followWaypoints(drone, waypoints):
	"""Commands a drone to follow a set of waypoints

	Args:
		drone: Drone ID
		waypoints: A list of waypoints to follow as tuples
	
	Returns:
		Something
	"""
	for point in waypoints:
		delay = drone.goToPoint(point)
		time.sleep(delay)
