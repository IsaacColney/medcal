import datetime

from models.date_models import DateModels
from models.pog_models import PogModels

DAYS_IN_MONTH : list[int] = [31,28,31,30,31,30,31,31,30,31,30,31]
TOTAL_DAYS_IN_MONTH : list[int] = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

def get_current_date() -> DateModels:
    today_date = DateModels()
    today = datetime.datetime.now()
    today_date.day = int(today.strftime("%d"))
    today_date.month = int(today.strftime("%m"))
    today_date.year = int(today.strftime("%Y"))
    return today_date

def user_date_to_date_model(user_input : str) -> DateModels:
    user_input_list = user_input.split("/")
    user_input_date = DateModels(int(user_input_list[0]) , int(user_input_list[1]) , int(user_input_list[2]))
    return user_input_date

def date_to_days(date : DateModels) -> int:
    days : int = 0
    for i in range(date.month):
        days += DAYS_IN_MONTH[i - 1]
    days -= date.day
    return days

def days_to_date(total_days : int , year : int) -> DateModels:
    date = DateModels()
    for i in range(12):
        if(total_days > TOTAL_DAYS_IN_MONTH[i-1] and total_days < TOTAL_DAYS_IN_MONTH[i]):
            date.month = i
    date.day = total_days - TOTAL_DAYS_IN_MONTH[date.month - 1]
    date.year = year
    return date
    
def pog_model_format(total_days : int) -> PogModels:
    weeks = int((total_days - total_days%7) / 7)
    days = total_days%7
    return PogModels(weeks , days)
    
def pog_calculator(lmp : DateModels):
    today : DateModels = get_current_date()
    pog : int = 0
    year_diff = today.year - lmp.year
    range_start = lmp.month
    range_stop = today.month + (12 * year_diff) 
    for i in range(range_start,range_stop):
        if(i%12 != 0):
            i = i%12
        else:
            i = 12
        pog += DAYS_IN_MONTH[i - 1]
    pog += (today.day - lmp.day)
    return pog_model_format(pog)

def edd_calculator(lmp : DateModels) -> DateModels:
    days = date_to_days(lmp)
    edd = DateModels()
    days += (40*7 - 8)
    if(days / 356 <= 1):
        edd = days_to_date(days , lmp.year)
    else:
        lmp.year += 1
        edd = days_to_date(days%356 , lmp.year)
    return edd
        
        
    
    
    



    
    
    