from udacidrone import Drone
from udacidrone.connection import MavlinkConnection
conn = MavlinkConnection('tcp:127.0.0.1:5760', threaded=True)
drone = Drone(conn)
drone.start()
drone.take_control()
drone.arm()
drone.takeoff(3)
drone.cmd_position(0,0,3,0)
global_to_local(drone._longitude, drone._latitude, 0)

def point(p):
    return np.array([p[0], p[1], 1.])
p1 = np.array([1., 2])
p2 = np.array([2, 3])
p3 = np.array([3, 3])
p4 = np.array([3, 4])
mat = np.vstack((point(p1), point(p2), point(p3)))
mat1 = np.vstack((point(p1), point(p2), point(p4)))
np.linalg.det(mat)
np.linalg.det(mat1)

