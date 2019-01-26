import numpy as np

import car
import track

class Game:
    def __init__(self, trackcsv, carcsv):
        self.track = np.loadtxt(open(track, "rb"), delimiter=",", skiprows=1)
        self.carsim = car.car(carfile)
        self.inplay = True
        self.distance = 0

    def play(self, action):
        self.inplay = self.carsim.evolve(track[distance], action)

    def get_score(self):
        return self.distance / self.carsim.time

    def is_over(self):
        return not self.inplay
    
    def is_won(self):
        return self.distance == len(self.track)

    def get_possible_actions(self):
        return list(range(0, self.carsim.breaking, -1)) + list(range(0, self.carsim.acceleration, 1))

def simulate(carfile, track, inst):
    instructions = np.loadtxt(open(inst, "rb"), delimiter=",", skiprows=1)
    track = np.loadtxt(open(track, "rb"), delimiter=",", skiprows=1)
    carsim = car(carfile)
    
    distance = 0
    while carsim.evolve(track[distance], instructions[distance]):
        print(distance, carsim.cur_v)
        distance += 1

    print("GOT TO: " + str(distance))

# simulate("data/sample_car.csv", "data/track_1.csv", "data/sample_instructions.csv")
