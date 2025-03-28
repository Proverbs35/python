# FILE NAME - for_loop_start_end.py

# NAME: Nate Cancel
# DATE: 3-6-2025
# BRIEF DESCRIPTION:  create show loop generator



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

#34wronggggr
def main():
    user_range()

def user_range():
    start = int(input('Starting point: '))
    end = int(input('Ending point: '))

    for x in range(start, end + 1):
        print(x, ' ', end='')

main()






########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Starting point: 3
Ending point: 7
3 4 5 6 7
'''


'''
Starting point: -4
Ending point: 4
-4 -3 -2 -1 0 1 2 3 4
'''


'''
Starting point: 0
Ending point: 1
0 1
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
[ ] I pretty much get it.
[X] I'm solid. Totally got it.

'''
