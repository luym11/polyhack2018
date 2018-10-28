import numpy as np
from multiprocessing import Value

SWARMNAME = "OKAY"
DRONES = [
	"24", "25", "26"
]
DRONEADDRS = {
	"24" : "E7E7E7E724",
	"25" : "E7E7E7E725",
	"26" : "E7E7E7E726"
}
SERVERIP = "10.4.14.28"
# Value(DRONEPOSITIONS,{
#     "24" : np.array([0,0,0]),
# 	"25" : np.array([0,0,0]),
# 	"26" : np.array([0,0,0])
# })
DRONEPOSITIONS = {
    "24" : np.array([0,0,0]),
	"25" : np.array([0,0,0]),
	"26" : np.array([0,0,0])
}
HOLDSTATE = {
 	"24" : False,
	"25" : False,
	"26" : False
}


