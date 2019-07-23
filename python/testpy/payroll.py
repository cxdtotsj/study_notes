

def pay(wage,sec_number=None,fund_number=None,sec_prop=None,fund_prop=None,fund_prop_two=None): 
    if sec_number == None:
        sec_number = wage
    if fund_number == None:
        fund_number = sec_number
    if sec_prop == None:
        sec_prop = 0.105
    if fund_prop == None:
        fund_prop = 0.07
    pay_sec = sec_number * sec_prop
    if fund_prop_two is not None:
        pay_fund = fund_number * (fund_prop + fund_prop_two)
    else:
        pay_fund = fund_number * fund_prop
    pay_number = wage - pay_sec - pay_fund - 5000
    aux_number = 0
    if pay_number <= 3000:
        aux_number = pay_number
    elif 3000<pay_number<=12000:
        tax_number = pay_number*0.1-210
        aux_number = pay_number - tax_number
    elif 12000<pay_number<=25000:
        tax_number = pay_number*0.2-1410
        aux_number = pay_number - tax_number 
    elif 25000<pay_number<=35000:
        tax_number = pay_number*0.25-2660
        aux_number = pay_number - tax_number     
    elif 35000<pay_number<=55000:
        tax_number = pay_number*0.3-4410
        aux_number = pay_number - tax_number
    elif 55000<pay_number<=80000:
        tax_number = pay_number*0.35-7160
        aux_number = pay_number - tax_number 
    elif pay_number>80000:
        tax_number = pay_number*0.45-15160
        aux_number = pay_number - tax_number
    return aux_number+5000


number = pay(wage=10000)
print(number)
    


a = ['a','b','c']
b = list(map(lambda x:x.upper(),a))
print(b)


