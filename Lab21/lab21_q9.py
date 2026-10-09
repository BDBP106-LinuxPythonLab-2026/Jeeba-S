import math
def population_growth(initial,rate,time):
    def exponential_growth():
        t=initial+math.exp(rate*time)
        return t
    pop = exponential_growth()
    r=round(pop,4)
    return r
print(population_growth(10,0.1,10))


