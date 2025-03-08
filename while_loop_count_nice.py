# FILE NAME - while_loop_count_nice.py

# NAME: Nate Cancel
# DATE: 3-7-2025
# BRIEF DESCRIPTION:  output range in a certain way



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

def print_to_nine():
    numbers = []  
    start = 0
    while start <= 9:
        numbers.append(start)  
        start += 1
    for num in numbers:
        if num != 9:
            print(num, end=", ")
        else:
            print(num, end="")
    return numbers

print_to_nine()
  

########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
'''



########################################
#            ATTESTATION
########################################

'''

It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[X] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
