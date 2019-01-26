import numpy as np

class track:
    def __init__(csv):
        self.track = np.loadtxt(open(csv, "rb"), delimiter=",", skiprows=1)

