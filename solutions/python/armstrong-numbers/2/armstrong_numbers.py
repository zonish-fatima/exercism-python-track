def is_armstrong_number(number):
    temp = number
    sum = 0
    power = len(str(number))

    while temp >0:
        #Extract the last digit
        digit = temp%10
        sum+=digit**power
        #Remove the last digit
        temp//=10

    if sum == number:
        return True
    return False

        
        
