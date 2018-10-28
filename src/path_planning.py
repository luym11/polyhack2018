import api

import math

import numpy as np



MAP = api.getArena()["buildings"]

# Make sure that the MAP has np.arrays of the obstacle coordinates!



# ASSUMES WAYPOINTS IS AN EMPTY LIST, make sure z = 0.3 in start and end

def generateWaypoints(start, end):

    # print(waypoints)

    waypoints = []

    dist_vec = end - start

    # print(dist_vec)

    # Determine number of intermediate points based on distance

    dist = np.linalg.norm(dist_vec)

    # N_p = int(7 * dist) + 1 #np.ceil(20*dist)

    # print("dist",dist)

    # print("N_p",N_p)

    N_p = 50 # HARDCODE, REMOVE!

    steps = np.linspace(0, 1, N_p)  # 0 to 1 with 1/N_p step_size

    # print(steps)

    # Create intermediate points

    x_coords = start[0] + steps*dist_vec[0]

    y_coords = start[1] + steps*dist_vec[1]

    z_coords = 0.3*np.ones((N_p,))



    coll_points = np.vstack([x_coords, y_coords, z_coords])

    # print(coll_points)

    N_obs = 4 # CHANGE

    col_detected = False



    point_col = np.zeros((N_p,), dtype=bool)

    point_col[0] = True

    point_col[-1] = True



    # Loop through all points and all obstacles

    for i in range(N_p):

        col_detected = [False, False, False, False]

        for j in range(N_obs):

            

            # Get the position of the jth obstacle

            obs_pos = MAP[j]

            # Build envelope around obstacles

            obs_limits = returnEnvelope(obs_pos)

            # Check for collision (ith point with all obstacles)

            col_detected[j] = isInSquare(coll_points[:,i], obs_limits)

            # If there is a collision, then move inner point to a corner

            # Afterwards, recursion!

            

            if col_detected[j]:

                new_point = movePointOut(coll_points[:,i], obs_pos)

                # if not np.array_equal(waypoints[-1], new_point):

                point_col[i] = 1

                waypoints.append(new_point)

                # print('appended0 %f, %f', (new_point[0], new_point[1]) )

    

        if(np.array_equal(np.asarray(col_detected), [False, False, False, False])):

            # print('appended1 %f, %f', (coll_points[0,i], coll_points[1,i]) )

            waypoints.append(coll_points[:,i])

        

    # print(point_col)

    # Stupid shit

    filt_wp = []

    for n in range(len(waypoints)):

        if point_col[n] == 1:

            filt_wp.append(waypoints[n])



    dupl_log = np.zeros((N_p,), dtype=bool)

    for l in range(len(filt_wp)):

        if l > 0:

            if np.array_equal(filt_wp[l], filt_wp[l-1]):

                dupl_log[l] = 1



    sec_filt_wp = []

    for k in range(len(filt_wp)):

        if dupl_log[k] == 0:

            sec_filt_wp.append(filt_wp[k])



    print(len(sec_filt_wp))



    return sec_filt_wp





# # While last waypoint is not equal to goal, continue recursion

# while(!np.array_equal(waypoints[-1], goal)):

#     collisionCheck(waypoints[-1], goal, waypoints)



# def generateWaypoints(start, end):

#     return [start, end]



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

    return (within_x and within_y)





def movePointOut(p, c):

    '''

    Move the points that are inside the obstacle envelope to 20cm outside

    of it's nearest corner



    Args:

        p: the point needs to be moved out

        c: center of the obstacle



    Returns:

        mp: the moved point

    '''

    r = 0.4 # radius of the envelope

    h = 0.3 # default height



    corners = []

    corners.append(np.asarray([c[0] - r * math.sqrt(2), c[1] + r * math.sqrt(2)])) # left up

    corners.append(np.asarray([c[0] - r * math.sqrt(2), c[1] - r * math.sqrt(2)])) # left down

    corners.append(np.asarray([c[0] + r * math.sqrt(2), c[1] + r * math.sqrt(2)])) # right up

    corners.append(np.asarray([c[0] + r * math.sqrt(2), c[1] - r * math.sqrt(2)])) # right down



    distances = [np.linalg.norm(corner_point - p[0:2]) for corner_point in corners]



    index = np.argmin(distances) # index of the minimum distance



    mp = [0, 0, h]

    mp[0:2] = corners[index]

    return mp



# print(movePointOut([5.1, 4.9, 3],[5, 5, 4]))



def returnEnvelope(c):

    '''

    This function takes the center point of the obstacle and returns an envelope indicating it's

    edge, namely x_min, x_max, y_min, y_max



    Args:

        c: center point of the obstacle we want to compute



    Returns:

        e: a list consisting [xmin, xmax, ymin, ymax]

    '''

    r = 0.4 # radius of the envelope



    e = []

    e.append(c[0] - r) # xmin

    e.append(c[0] + r) # xmax

    e.append(c[1] - r) # ymin

    e.append(c[1] + r) # ymax

    return e