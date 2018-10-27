import api
import globals
import numpy

backlog = []
destinations = []

def getDstPoint(pkg):
	"""Determines the index of the package's destination point

	Args:
		pkg: The dictionary of the package data
	
	Returns:
		Index of the package's destination, if known
	"""
	global destinations
	i = 0
	for dst in destinations:
		if pkg["coordinates"] == dst:
			return i
		i += 1
	return -1

def refillQueue():
	"""Refills the backlog of ordered parcel deliveries
	"""
	global backlog
	global destinations
	if len(backlog) < 20:
		for _ in range(20 - len(backlog)):
			package = api.package(globals.SWARMNAME)
			backlog.append(package)
	# update list of destinations, if necessary
	if len(destinations) < 8:
		for pkg in backlog:
			if pkg["coordinates"] not in destinations:
				destinations.append(pkg["coordinates"])

def getBestBundle(home):
	"""Gets the most profitable bundle of packages to deliver

	Args:
		home: Location of the home base for the drone as a numpy array
	
	Returns:
		List of the most profitable packages to deliver
	"""
	global backlog
	global destinations
	sameDest = [[
		pkg for pkg in backlog if pkg["coordinates"] == dst
	] for dst in destinations]
	profitable = [
		bundle for bundle in sameDest if len(bundle) >= 3
	]
	profitable = sorted(
		profitable,
		key=lambda pkgs: numpy.linalg.norm(home - numpy.array([
			pkgs[0]["coordinates"]
		]))
	)
	profitable = profitable[0][:3]
	backlog = [
		pkg for pkg in backlog if (True not in [pkg["id"] == profit["id"] for profit in profitable])
	]
	return profitable
