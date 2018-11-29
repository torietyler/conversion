'''
convert from f to c and from c to f
'''
degree = input("enter c for celsius, or f for fahreiheit :")
temperature = int(input("Enter the temperature value :"))

if degree == 'f':
    C = (temperature - 32)*5/9
    print("the temperature in celsius is :", round (C))
elif degree == 'c':
    F = temperature*9/5 + 32
    print("the temperature in fahreiheit :", round (F))
else :
    print("there is no such type of degree like :", degree)
exit()