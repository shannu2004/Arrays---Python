def plusOne(digits):
    str_digit=""
    for d in digits:
        str_digit=str_digit+str(d)
    digit_int = int(str_digit)+ 1
    str_digit=str(digit_int)
    result=[]
    for s in str_digit:
        result.append(int(s))
    return result
digits=[1,2,3]
print(plusOne(digits))
