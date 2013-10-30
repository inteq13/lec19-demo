import matplotlib.pyplot as pt
import numpy as np
import modepy as mp

nodes = mp.warp_and_blend_nodes(2, 10)
pt.plot(nodes[0], nodes[1], "x")

tri = np.array([(-1, -1), (1, -1), (-1, 1), (-1, -1)]).T
pt.plot(nodes[0], nodes[1], "x")
pt.plot(tri[0], tri[1], "-b")
pt.gca().set_aspect("equal")
pt.show()
