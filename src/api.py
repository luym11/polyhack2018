import urllib.request
import json

def makeGET(request):
	"""Makes a GET request to the server

	Args:
		request: The request URL, excluding '/api/'
	
	Returns:
		The server's response
	"""
	return json.loads(
		urllib.request.urlopen("http://10.4.14.28:5000/api/{0}".format(request)).read().decode("utf-8")
	)

def getArena():
	"""Gets the arena data

	Returns:
		Server response for /api/arena
	"""
	return makeGET("arena")

def package(swarm):
	"""Orders a new package for the swarm

	Args:
		swarm: Swarm ID

	Returns:
		Server response
	"""
	return makeGET("{0}/package".format(swarm))

def printDeliveries(swarm):
	"""Obtains the delivery stats for the swarm

	Args:
		swarm: Swarm ID
	
	Returns:
		Server response
	"""
	return makeGET("{0}/print_deliveries".format(swarm))

def registerSwarm(name, arena, seed):
	"""Registers a swarm with the given properties

	Args:
		name: Swarm ID
		arena: Arena ID
		seed: RNG seed
	
	Returns:
		Server response
	"""
	return makeGET("{0}/register_swarm?arena_id={1}&seed={2}".format(name, arena, seed))

def resetSeed(swarm, seed):
	"""Resets the RNG seed

	Args:
		swarm: Swarm ID
		seed: New RNG seed

	Returns:
		Server response
	"""
	return makeGET("{0}/reset_package_generator?seed={1}".format(swarm, seed))

def swarmStatus(swarm):
	"""Gets the status of all drones in the swarm

	Args:
		swarm: Swarm ID

	Returns:
		Server reponse
	"""
	return makeGET("{0}/status".format(swarm))

def calibrateDrone(swarm, drone):
	"""Calibrates a drone in the swarm

	Args:
		swarm: Swarm ID
		drone: Drone ID

	Returns:
		Server response
	"""
	return makeGET("{0}/{1}/calibrate".format(swarm, drone))

def connectDrone(swarm, drone, address):
	"""Connects a drone

	Args:
		swarm: Swarm ID
		drone: Drone ID/number
		address: Drone address

	Returns:
		Server response
	"""
	return makeGET("{0}/{1}/connect?r=0&c=94&a={2}&dr=2M".format(swarm, drone, address))

def deliver(swarm, drone, package):
	"""Sends a delivery request for a package

	Args:
		swarm: Swarm ID
		drone: Drone ID
		package: Package ID
	
	Returns:
		Server response
	"""
	return makeGET("{0}/{1}/deliver?package_id={2}".format(swarm, drone, package))

def disconnectDrone(swarm, drone):
	"""Disconnects a drone

	Args:
		swarm: Swarm ID
		drone: Drone ID

	Returns:
		Server response
	"""
	return makeGET("{0}/{1}/disconnect".format(swarm, drone))

def droneGoto(swarm, drone, x, y, z, yaw, velocity):
	"""Commands a drone to fly to a given location

	Args:
		swarm: Swarm ID
		drone: Drone ID
		x, y, z: Target coordinates
		yaw: Desired yaw
		velocity: Movement velocity
	
	Returns:
		Server reponse
	"""
	return makeGET("{0}/{1}/goto?x={2}&y={3}&z={4}&yaw={5}&v={6}".format(swarm, drone, x, y, z, yaw, velocity))

def land(swarm, drone, height, velocity):
	"""Commands a drone to land

	Args:
		swarm: Swarm ID
		drone: Drone ID
		height: Height of the target landing area
		velocity: Landing velocity
	
	Returns:
		Server response
	"""
	return makeGET("{0}/{1}/land?z={2}&v={3}".format(swarm, drone, height, velocity))

def droneStatus(swarm, drone):
	"""Gets a drone's status

	Args:
		swarm: Swarm ID
		drone: Drone ID
	
	Returns:
		Drone status
	"""
	return makeGET(swarm, drone)

def stopDrone(swarm, drone):
	"""Commands a drone to stop

	Args:
		swarm: Swarm ID
		drone: Drone ID
	
	Returns:
		Server response
	"""
	return makeGET("{0}/{1}/stop".format(swarm, drone))

def takeoff(swarm, drone, height, velocity):
	"""Commands a drone to take off

	Args:
		swarm: Swarm ID
		drone: Drone ID
		height: Desired final height
		velocity: Takeoff velocity
	
	Returns:
		Server response
	"""
	return makeGET("{0}/{1}/takeoff?z={2}&v={3}".format(swarm, drone, height, velocity))
