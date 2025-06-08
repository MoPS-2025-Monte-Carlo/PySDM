import math

class MonteCarlo:
    def __init__(self, _):
        pass

    @staticmethod
    def displacement(_, position_in_cell, c_l, c_r, u01):
        c = max(c_l, c_r)
        probability_of_shift = abs(c)
        guaranteed_shift = int(probability_of_shift // 1)
        probability_of_shift -= guaranteed_shift

        sign = int(abs(c) / c)
        return position_in_cell + (guaranteed_shift * sign) + (probability_of_shift > u01) * sign
