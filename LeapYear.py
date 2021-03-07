def LeapYear(x):
    if(x/4.0 == round(x/4.0)):
        if(x/100.0 == round(x/100.0)):
            if(x/400.0 == round(x/400.0)):
                    return True
            return False
        return True
    return False
    
