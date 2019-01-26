import numpy as np

MAP_GAS = [-1, 500, 750, 1000, 1250, 1500]
MAP_TIRE = [-1, 500, 750, 1000, 1250, 1500]
MAP_HANDLING = [-1, 9, 12, 15, 18, 21]

class car:
    def __init__(self, csv):
        parsed = np.loadtxt(open(csv, "rb"), dtype=int, delimiter=",", skiprows=1)
        self.tire = MAP_TIRE[parsed[0]]
        self.gas = MAP_GAS[parsed[1]]
        self.handling = MAP_HANDLING[parsed[2]]
        self.speed = parsed[3]
        self.acceleration = parsed[4]
        self.breaking = parsed[5]

        self.cur_v = 0
        self.cur_gas = self.gas
        self.cur_tire = self.tire
        self.time = 0

    # inst = [acc, pit_stop]
    def evolve(self, radius, inst):
        pit_stop = inst[1] == 1

        if radius == -1:
            v_max = -1
        else:
            v_max = np.sqrt(radius * self.handling / 1000000)

        if pit_stop:
            self.time += 30
            self.cur_v = 0
            self.cur_gas = self.gas
            self.cur_tire = self.tire
            return False

        if inst[0] == 0:
            self.time += 1 / self.cur_v
            return True

        if self.gas == 0:
            inst[0] = 0

        v_1sq = self.cur_v ** 2 + 2 * inst[0]
        if v_1sq > 0:
            v_1 = np.sqrt(v_1sq)
        else:
            v_1 = 0
        
        if v_max != -1 and max(v_1, self.cur_v) > v_max:
            print("max speed exceeded")
            return False

        self.time += (v_1 - self.cur_v) / inst[0]
        self.cur_v = v_1
        if inst[0] > 0:
            self.gas -= 0.1 * inst[0] ** 2
        else:
            self.tire -= 0.1 * inst[0] ** 2

        if self.gas < 0:
            self.gas = 0

        if self.tire < 0:
            print("tire ran out")
            return False

        return True


        
