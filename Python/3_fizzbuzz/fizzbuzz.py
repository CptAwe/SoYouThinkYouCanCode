"""
In a range of numbers, for each number print "fizz" if it is
perfectly divided by 3, "buzz" if it is perfectly divided by
5 and "fizzbuzz" if it perfectly divided by both.

In any other situation print the number.
"""


for i in range(1, 255):
    output = ""
    if i%3 == 0:
        output += "fizz"
    if i%5 == 0:
        output += "buzz"
    
    if output == "":
        output = i
    
    print(output)
    


