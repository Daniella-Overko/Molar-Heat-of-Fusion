msys = float(input("Enter msys (without uncertainty or unit): "))
msys_uncertainty = float(input("Enter msys uncertainty (without unit): "))
c = 4.18
print("I'll use the c (specific heat capacity) of water for both the sys and the surr")
T_change_sys = float(input("Enter ΔTsys: "))
T_change_sys_uncertainty = float(input("Enter ΔTsys uncertainty: "))
msurr = float(input("Enter msurr: "))
msurr_uncertainty = float(input("Enter msurr uncertainty: "))
T_change_surr = float(input("Enter ΔTsurr: "))
T_change_surr_uncertainty = float(input("Enter ΔTsurr uncertainty: "))
molar_mass = 18.02
print("I had the molar mass of the system as 18.02, since I assumed it's water")

Qsurr_half = msurr * c 
Qsurr = Qsurr_half * T_change_surr
negative_n_H_change = Qsurr + msys * c * T_change_sys
n_H_change = negative_n_H_change * -1
H_change = n_H_change/(msys/molar_mass)
print(f"The molar heat of fusion should be {H_change}J/mol! ✨ (convert to kJ/mol yourself)")

Qsurr_uncertainty_percent=(((msurr_uncertainty*c)/Qsurr_half)*100.0)+(((T_change_surr_uncertainty/(T_change_surr*-1)))*100.0)
Qsurr_uncertainty=Qsurr_uncertainty_percent/100.0*(Qsurr*-1)
n_H_change_uncertainty_percent=(((msys_uncertainty*c)/(msys*c))*100.0)+(((T_change_sys_uncertainty/T_change_sys))*100.0)
n_H_change_uncertainty=Qsurr_uncertainty+((n_H_change_uncertainty_percent/100.0)*(msys*c*T_change_sys))

H_change_uncertainty_percent=(n_H_change_uncertainty/n_H_change*100.0)+(msys_uncertainty/molar_mass/(msys/molar_mass)*100.0)
H_change_uncertainty=H_change_uncertainty_percent/100.0*H_change
input(f"The uncertainty should be {H_change_uncertainty} 😀 (for J/mol)")

