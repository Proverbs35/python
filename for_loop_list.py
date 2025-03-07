# FILE NAME - for_loop_list.py

# NAME: Nate Cancel
# DATE: 3-6-2025
# BRIEF DESCRIPTION:  make list of dogs 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

########## ENTER YER CODE BELOW THIS LINE ##########


def main():
    doggo_names = get_doggo_names()
    output_names(doggo_names)

def get_doggo_names():
    name = ''
    names = []
    while name != 'DONE':
        name = input('Name of doggo: ')
        if name != 'DONE':
            print(f'{name} is awesome.')
    
    return names
print(f'{name} is awesome.')

def output_names(doggo_names):
    print()

main()
    
  ########### END YER CODE ABOVE THIS LINE ##########

########################################
#          SAMPLE OUTPUT
########################################

'''
Name of doggo: Maggie
Name of doggo: Quinnie
Name of doggo: Yogi
Name of doggo: BB-8
Name of doggo: DONE

Maggie is awesome.
Quinnie is awesome.
Yogi is awesome.
BB-8 is awesome.
'''


'''
Name of doggo: a
Name of doggo: b
Name of doggo: c
Name of doggo: DONE

a is awesome.
b is awesome.
c is awesome.
'''


'''
Name of doggo: DONE
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
[ ] I'm solid. Totally got it.

'''
