def get_min_max(ints):
    if len(ints)==0:
        return None
    min_=ints[0]
    max_=ints[0]
    for i in ints:
        if i<min_:
            min_=i
        if i>max_:
            max_=i
            
    return(min_,max_)
    
import random

l = [i for i in range(0, 10)]  
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(-12, 25)]  
random.shuffle(l)
print("Pass" if ((-12, 24) == get_min_max(l)) else "Fail")
l = [i for i in range(300, 301)]  
random.shuffle(l)
print("Pass" if ((300, 300) == get_min_max(l)) else "Fail")
l = []  
print("Pass" if (None == get_min_max(l)) else "Fail")
l = [i for i in range(-24, -1)]  
random.shuffle(l)
print("Pass" if ((-24, -2) == get_min_max(l)) else "Fail")
