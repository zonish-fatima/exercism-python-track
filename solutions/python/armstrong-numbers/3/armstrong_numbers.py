def is_armstrong_number(number):
    temp = number
    result = 0
    power = len(str(number))

    while temp >0:
        #Extract the last digit
        digit = temp%10
        result+=digit**power
        #Remove the last digit
        temp//=10

    if result == number:
        return True
    return False

        
        
