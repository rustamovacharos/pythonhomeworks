def factor_of_number(number):
    factor = [(num)for num in range(1,number+1) if number%num==0]
    print(factor,"is a factor of ",number )
print(factor_of_number(12))
