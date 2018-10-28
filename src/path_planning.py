import api
import math
import numpy as np

safety = 0.3
MAP = api.getArena()["buildings"]
# Make sure that the MAP has np.arrays of the obstacle coordinates!

# ASSUMES WAYPOINTS IS AN EMPTY LIST, make sure z = 0.3 in start and end
def generateWaypoints(start, end):
	waypoints = []
	height = start[2]
	dist = end - start
	grad = 1000000000
	if dist[0] != 0:
		grad = dist[1] / dist[0]

	# Loop through all points and all obstacles
	for obstacle in MAP:
		if alongPath(start, obstacle, end):
			print("along path")
			localSafetyX, localSafetyY = safety, safety
			x0, x1, y0, y1 = returnEnvelope(obstacle)
			xo, xf = x0, x1
			if start[0] >= x1:
				print("coming from the right")
				xo, xf = xf, xo
				localSafetyX *= -1
			yo, yf = y0, y1
			if start[1] >= y1:
				yo, yf = yf, yo
				localSafetyY *= -1
			oldLen = len(waypoints)
			print(yo, grad * (xo - start[0]) + start[1], yf)
			if between(yo, grad * (xo - start[0]) + start[1], yf):
				print("hitting the side")
				waypoints += [
					np.array([
						xo - localSafetyX, yo - localSafetyY, height
					]),
					np.array([
						xo - localSafetyX, yf + localSafetyY, height
					])
				]
			elif between(xo, (yo - start[1]) / grad + start[0], xf):
				waypoints += [
					np.array([
						xo - localSafetyX, yo - localSafetyY, height
					]),
					np.array([
						xf + localSafetyX, yo - localSafetyY, height
					])
				]
			if len(waypoints) > oldLen:
				waypoints += generateWaypoints(waypoints[-1], end)
 
	if len(waypoints) == 0:
		waypoints.append(end)
	return waypoints

def alongPath(a, b, c):
	return between(a[0], b[0], c[0]) and between(a[1], b[1], c[1])

def between(a, b, c):
	return (a <= b <= c) or (a >= b >= c)

# Give obstacle position and compute x_min/max bounds here?
def isInSquare(point, limits):
	x_pos = point[0]
	y_pos = point[1]

	# Confirm ordering with returnEnvelope function!
	x_min = limits[0]
	x_max = limits[1]
	y_min = limits[2]
	y_max = limits[3]

	within_x = (x_pos < x_max and x_pos > x_min)
	within_y = (y_pos < y_max and y_pos > y_min)
	if within_x and within_y:
		return True
	else:
		return False

def returnEnvelope(c):
	'''
	This function takes the center point of the obstacle and returns an envelope indicating it's
	edge, namely x_min, x_max, y_min, y_max

	Args:
		c: center point of the obstacle we want to compute

	Returns:
		e: a list consisting [xmin, xmax, ymin, ymax]
	'''
	r = 0.2 # radius of the envelope

	e = []
	e.append(c[0] - r) # xmin
	e.append(c[0] + r) # xmax
	e.append(c[1] - r) # ymin
	e.append(c[1] + r) # ymax
	return e
