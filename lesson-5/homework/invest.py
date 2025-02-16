principal_amount = 100
rate =5
def invest(amount,rate,years):
   invested = (amount*((100+rate)/100))
   rounded= round(invested,2)
   print(rounded)
print(invest(134,5,2015))