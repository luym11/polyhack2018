import api
import globals

class Drone:
	"""Creates a new Drone object

	Args:
		id: Drone ID
		addr: Drone address
	"""
	def __init__(id, addr):
		self.droneID = id
		self.droneAddr = addr
		status = api.connectDrone(globals.SWARMNAME, id, addr)
		status = api.droneStatus(globals.SWARMNAME, id)
		self.pos = (status["x"], status["y"], status["z"])
		self.home = self.pos
		self.packages = []
		self.currentDelivery = ""

	def disconnect(self):
		"""Disconnects the drone from the server

		Returns:
			Whether the disconnect succeeded
		"""
		status = api.disconnectDrone(globals.SWARMNAME, self.droneID)
		return status["success"]
	
	def update(self):
		status = api.droneStatus(globals.SWARMNAME, self.droneID)
		self.pos = (status["x"], status["y"], status["z"])

	def goToPoint(self, point):
		"""Commands the drone to fly to a given point

		Args:
			point: The destination point as a tuple (x, y, z)

		Returns:
			Estimated travel time before the drone reaches the point
		"""
		resp = api.droneGoto(globals.SWARMNAME, self.droneID, point[0], point[1], point[2], 0, 1)
		return resp["duration"]
	
	def getPackage(self, package):
		"""Picks up a new package

		Args:
			package: Package data of new package

		Returns:
			If the package was picked up successfully, the amount of weight that can
			still be carried by the drone. Otherwise, -1.
		"""
		totalWeight = sum([pkg["weight"] for pkg in self.packages])
		if totalWeight + package["weight"] > 3:
			return -1
		self.packages.append(package)
		return totalWeight - package["weight"]
	
	def deliver(self):
		"""Attempts to deliver the current package

		Returns:
			Whether the delivery succeeded
		"""
		if self.currentDelivery != "":
			resp = api.deliver(globals.SWARMNAME, self.droneID, self.currentDelivery)
			return resp["success"]
