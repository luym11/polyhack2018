# Differences between API calls and Python wrapper functions

All functions use camelCase instead of underscores.

Unless otherwise specified, all functions take the same arguments as the API call, in the same order.

| API call | Python function |
| --- | --- |
| `/api/arena` | `getArena` |
| `/api/stop` | `stopDrone` |
| `/api/status` | `droneStatus` |
| `/api/goto` | `droneGoto` |
| `/api/disconnect` | `disconnectDrone` |
| `/api/connect` | `connectDrone(swarm, drone, address)` |
| `/api/calibrate` | `calibrateDrone` |
| `/api/status` | `swarmStatus` |
| `/api/reset_package_generator` | `resetSeed` |
