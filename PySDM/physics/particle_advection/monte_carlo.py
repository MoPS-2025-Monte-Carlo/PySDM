class MonteCarlo:
    def __init__(self, _):
        pass

    @staticmethod
    def displacement(_, position_in_cell, cell_id, c_l, c_r, u01):
        c = max(c_l, c_r)
        probability_of_shift = abs(c)
        assert (
            probability_of_shift
            < 1
        )

        sign = int(abs(c) / c)
        return cell_id + (probability_of_shift > u01) * sign
