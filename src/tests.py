import path_planning as pp
import api
import numpy as np
import matplotlib.pyplot as plt


print(A)
# MAP = api.getArena()["buildings"]
#
# wp = []
# new_wp = pp.generateWaypoints( np.array([0.5,1,0.5]), np.array([2.3,1,0.5]), wp )
#
# # print(len(new_wp))
# # print(new_wp[0][0])
# bla = np.asarray(new_wp)
# print(bla)
#
# # plot
# fig = plt.figure()
# ax = fig.gca()
# # fire plotting starts
# min_val, max_val = 0, 4
# # ax.matshow(intersection_matrix, cmap=plt.cm.Reds, origin='lower')
# ax.set_xticks(np.arange(0,4,1))
# ax.set_yticks(np.arange(0,4,1))
# plt.xlim(0,4)
# plt.ylim(0,4)
# plt.plot(bla[:,0], bla[:,1])
# plt.grid(linestyle = '--')
# plt.show()
# # print(new_wp[2])
#
# # print(returnEnvelope([4,5,3]))
#
# # collisionCheck(np.array([0,0]), np.array([1,1]))
# #print(np.shape(MAP["buildings"]))
# # print(np.shape(MAP))
# # print(MAP[0])
# # First element of tuple is number of obstacles!
# # print(MAP[0])
