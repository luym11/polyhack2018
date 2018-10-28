import globals
import api
import time
import drone

def followWaypoints(drone, waypoints, trajectories):
	"""Commands a drone to follow a set of waypoints

	Args:
		drone: Drone ID
		waypoints: A list of waypoints to follow as tuples
	
	Returns:
		Something
	"""
	for point in waypoints:
		drone.update()
		for id in globals.DRONES:
			if id not in trajectories:
				continue
			if id == drone.droneID:
				continue
			trajectory = trajectories[id]
			if "s0" not in trajectory:
				continue
			s0, sf = trajectory["s0"], trajectory["sf"]
			r0, rf = drone.pos, point
			ds = sf - s0
			dr = rf - r0
			if (r0[0] - s0[0]) / (ds[0] - dr[0]) == (r0[1] - s0[1]) / (ds[1] - dr[1]):
				time.sleep(trajectory["dt"] - (time.time() - trajectory["t0"]))
		delay = drone.goToPoint(point)
		trajectory[drone.droneID] = {
			"t0" : time.time(),
			"dt" : delay,
			"s0" : drone.pos,
			"sf" : point
		}
		time.sleep(delay)
