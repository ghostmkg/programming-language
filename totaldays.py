def get_days_in_month(month):

    days_in_month = {
        1: 31,  
        2: 28,  
        3: 31,  
        4: 30,  
        5: 31,  
        6: 30,  
        7: 31,  
        8: 31,  
        9: 30,  
        10: 31, 
        11: 30, 
        12: 31  
    }
    
    return days_in_month.get(month, "Invalid month number")

month_number = int(input().strip())
print(get_days_in_month(month_number))