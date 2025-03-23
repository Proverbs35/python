# FILE NAME - while_loop_guess_high_low.py

# NAME: Nate Cancel
# DATE: 3-12-2025
# BRIEF DESCRIPTION: guess that number



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




SECRET_NUMBER = 33


########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    secret_number = 33
    tries = 0
    guess = 0

    while guess != secret_number:
        guess = int(input("Guess a number: "))
        tries += 1
        
        if guess < secret_number:
            print('Your guess is too low.\n')
        elif guess > secret_number:
            print('Your guess is too high.\n')

    print(f'\nYou guessed in {tries} tries.')

main()



########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Guess a number: 22
Your guess is too low.

Guess a number: 44
Your guess is too high.

Guess a number: 33

You guessed in 3 tries.
'''


'''
Guess a number: 33

You guessed in 1 tries.Guess a number: -9
Your guess is too low.

Guess a number: 100
Your guess is too high.

Guess a number: 30
Your guess is too low.

Guess a number: 32
Your guess is too low.

Guess a number: 34
Your guess is too high.

Guess a number: 33

You guessed in 6 tries.
'''


'''
Guess a number: -9
Your guess is too low.

Guess a number: 100
Your guess is too high.

Guess a number: 30
Your guess is too low.

Guess a number: 32
Your guess is too low.

Guess a number: 34
Your guess is too high.

Guess a number: 33

You guessed in 6 tries.
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
