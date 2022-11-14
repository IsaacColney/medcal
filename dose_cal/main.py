def dose_calculator_tablet(drug_dose : int , requirement_dose : int , weight : float):
    return (weight * requirement_dose) / drug_dose

print(dose_calculator_tablet(625 , 25 , 70)) 