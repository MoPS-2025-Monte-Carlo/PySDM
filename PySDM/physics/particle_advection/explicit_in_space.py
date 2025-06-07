"""
basic explicit-in-space Euler scheme
"""
from .monte_carlo import MonteCarlo

class ExplicitInSpace:  # pylint: disable=too-few-public-methods
    def __init__(self, _):
        pass

    @staticmethod
    def displacement(_, position_in_cell, cell_id, c_l, c_r, use_monte_carlo, u01):
        if use_monte_carlo:
            return MonteCarlo.displacement(_, position_in_cell, cell_id, c_l, c_r, u01)
        return c_l * (1 - position_in_cell) + c_r * position_in_cell
