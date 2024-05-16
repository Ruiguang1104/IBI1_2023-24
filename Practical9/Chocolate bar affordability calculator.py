def chocolate_calculate():
    total_money=input('input your money:')
    price=input('price:')
    total_money1=int(total_money)
    price1=int(price)
    #make the two variable can be calculated
    number=total_money1/price1
    #calculate the number of chocolate he or she can buy
    remain_money=total_money1%price1
    #calculate the remaining money
    return number, remain_money
number, remain_money = chocolate_calculate()
print(f"Number of chocolates you can buy: {int(number)}")
print(f"Remaining money: {remain_money}")