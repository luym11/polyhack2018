import api
import numpy as np

MAP = api.getArena()

# Make sure that the MAP has np.arrays of the obstacle coordinates!

def collisionCheck(start, end, obs_rad):
    coll_points = np.array([])
    dist_vec = end - start

    # dist = np.linalg.norm(dist_vec)
    # N_p = round(dist / 10, 0)
    N_p = 10
    step_size = 1.0/N_p
    coll_points = [step_size*i for i in range(N_p)]

    return

def generateWaypoints(start, end):
    return [start, end]
