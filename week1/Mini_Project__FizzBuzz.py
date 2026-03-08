#Mini Project: FizzBuzz
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)




#Print numbers 1 to 30, BUT:
    #If the number is divisible by 3, print "Fizz" instead
    #If the number is divisible by 5, print "Buzz" instead
    #If divisible by BOTH 3 and 5, print "FizzBuzz" instead
    #Otherwise just print the number