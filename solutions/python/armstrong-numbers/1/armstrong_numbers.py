def is_armstrong_number(number):
    temp = number
    length = len(str(number))
    sum  = 0
    while temp > 0:
        #Extract the last digit of the number
        digit = temp%10
        sum+= digit**length
        #Remove the last digit from the number
        temp//=10 
        
    if sum == number:
        return True
    return False
        
        
        


        
