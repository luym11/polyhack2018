import globals

def followWaypoints(waypoints, drone):
	"""Commands a drone to follow a set of waypoints

	Args:
		waypoints: A list of waypoints to follow as tuples
		drone: Drone ID
	
	Returns:
		Something
	"""
	for point in waypoints:
		#
