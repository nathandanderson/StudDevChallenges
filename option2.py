# Nathan Anderson's Application for the Student Software Developer Position
# I hope you enjoy the code below! I'd love to hear back from you!


# Reverse String function declaration
def reverseString(sMyString):
    # List from inputted string
    lChars = list(sMyString)
    # Length of string for loop
    i = (len(lChars)-1)
    # Initializing variable 'output'
    output = ''
    # Loop counting down and assigning the positions from the list to spots in our final string in reverse order
    while i >= 0:
        output += lChars[i]
        i-=1
    return(output)



# Highest integer function declaration
    # Note: I know there is a max function that I believe can be used for this, but I was
    # concerned that using it was a little too easy, so here's how I would do it without that function.
def highestInteger(x, y, z):
    x = int(x)
    y= int(y)
    z = int(z)
    # Finds the max of the values that were inputted
    if x > y and x > z:
        return(x)
    elif y > x and y > z:
        return(y)
    else:
         return(z)



# Factorial function declaration
# I know that you want it with recursion, I didn't see that at first 
# so here was my initial function, below you can find the one with recurion.
def factorial (n):
    # Converting input to int and initializing array where values will be stored.
    n = int(n)
    aMultipliers = []
    # Adding all previous numbers to an array for later calculation
    while n > 0:
        aMultipliers.append(n)
        n-=1
    # Reading the array and multiplying all numbers including original number by lower values in array.
    x = 0
    output = 1
    while x < len(aMultipliers):
        output = output * aMultipliers[x]
        x+=1
    return(output)



# Attempt 2 at factorials (I admittedly did not see you wanted us to do it with recurion initially so I created this one with recursion.)
def factorialRecursion(n):
    # Converting input to int and verifying whether output exists in a given iteration or not.
    n = int(n)
    try:
        output
    except NameError:
        output = 1
    # If n = 1 then that means we are done and can return the output
    if n == 1:
        return(output)
    # If n >1 then that means we will continue with our recursion.
    else:
        output = n*factorialRecursion(n-1)
        return(output)






# Fibonacci Function declaration
def fibonacci (n):
    # Converts input to Integer then initializes variables
    n = int(n)
    x=0
    z=y=output=1
    # Loop to go through and continue adding numbers together until you reach the specified integer.
    while z < n:
        # Each number is a sum of the previous 2 numbers
        output = x+y
        # Reassign the newer value to be the older value
        x=y
        # Reassign the current value to be the newer value
        y=output
        # Increase the counter
        z+=1
    return(output)



# Prompting the user to enter the given information
print("Reversing a String")
print(reverseString(input("What string would you like reversed? ")) + '\n')
print("Selecting the highest of 3 Integers:")
print(str(highestInteger(input("Please enter the first Integer: "),input("Please enter the second Integer: "),input("Please enter the third Integer: "))) + '\n')
print("Calculating Factorials without Recursion")
print(str(factorial(input("What number would you like to calculate the factorial of? "))) + '\n')
print("Calculating Factorials using Recursion")
print(str(factorialRecursion(input("What number would you like to calcualte the recursive factorial of? "))) + '\n')
print("Calculating a given value of the Fibonacci Sequence")
print(str(fibonacci((input("What entry of the fibonacci sequence would you like to know? ")))) + '\n')
