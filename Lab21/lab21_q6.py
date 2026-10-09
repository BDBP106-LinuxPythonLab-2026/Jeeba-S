def cell_metabolism(glucose,oxygen):
    def energy_output():
        g_limit=glucose
        o_limit=oxygen/6
        r=min(g_limit,o_limit)
        return r*38
    return energy_output()
print(cell_metabolism(1,6))
print(cell_metabolism(5,6))
print(cell_metabolism(2,12))
