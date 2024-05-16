def James_Bond(birth_year):
    age1=int(birth_year)
#made it can be calculate
    age_movie=age1+18
    if age_movie>=1973 and age_movie<=1986:
        a='Roger Moore'
    elif age_movie>=1984 and age_movie<=1994:
        a='Timothy Dalton'
    elif age_movie>=1995 and age_movie<=2005:
        a='Pierce Brosnan'
    elif age_movie>=2006 and age_movie<=2021:
        a='Daniel Craig'
    return a
#return the name of the actor
user_birth_year = input('Please enter your birth year: ')
bond_actor = James_Bond(user_birth_year)
print(f'The James Bond actor for your age group is: {bond_actor}')
#have done it!