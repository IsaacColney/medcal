import os

from utils.obs_utils import user_date_to_date_model , pog_calculator , get_current_date , edd_calculator , user_date_to_date_model
from utils.term_checker import check_term

def pog_cal():
    today = get_current_date()
    input_lmp = input(f"Enter your pog : eg ( {today.day}/{today.month}/{today.year}) : ")
    lmp = user_date_to_date_model(input_lmp)
    pog = pog_calculator(lmp)
    print(f"POG : {pog.weeks} weeks {pog.days} days")
    print(f"{check_term(pog.weeks)} Pregnancy")
    input()
    
def edd_cal():
    today = get_current_date()
    input_lmp = input(f"Enter your edd : eg ( {today.day}/{today.month}/{today.year}) : ")
    lmp = user_date_to_date_model(input_lmp)
    edd = edd_calculator(lmp)
    print(f"EDD : {edd.day}/{edd.month}/{edd.year}")
    input()

def main():
    while(True):
        os.system("cls")
        print("""Select calculation:
            1: POG calculator
            2: EDD calculator
            """)
        user_input = int(input(" Enter : "))
        if(user_input == 1):
            pog_cal()
        elif(user_input == 2):
            edd_cal()
        else:
            print("Enter a correct input !!")
            
if __name__ ==  "__main__":
    main()
            
        
            
        
    
    
    
    