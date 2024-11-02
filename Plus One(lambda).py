def plusOne(digits):
    string =''.join(map(lambda x: str(x), digits))
    num = int(string)+1
    res = list(str(num))
    return [int(x) for x in res]
digits=[4,3,2,1]
print(plusOne(digits))
