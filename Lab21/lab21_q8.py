u1 = float(input("enter the temperature: "))
u2 = float(input("enter the enthalpy: "))
u3 = float(input("enter the entropy: "))
def protein_energy_temp(temp):
    k= temp+273.15
    def calculate_free_energy(enthalpy,entropy):
        g=enthalpy-(entropy*k)
        if g<0:
            print("stable")
        else:
            print("not stable")
        return g
    print(calculate_free_energy(u2,u3))
print(protein_energy_temp(u1))
#stable(25,10000,100)
#unstable(25,100000,100)
