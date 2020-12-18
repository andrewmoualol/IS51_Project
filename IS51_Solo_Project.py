"""
Begin will generate a random integer betweem 1 and 15, and 
based on the result of the random number, check to see if it falls under certain range
if the number is geater than 50, then the result will be "Emperor's Coin"
otherwise if the number is > 40, then the result will be "Noble's Coin"
otherwise if the number is > 30, then the result will be "Knight's Coin"
otherwise if the number is > 20, then the result will be "Footman's Coin"
otherwise if the number is > 10, then the result will be "Peasant's Coin"
otherwise if the number is not any of the above, then the result will be "Chaos Coin"

iterate over using a loop three times and print the results to the user. As an example "Peasant Footman Knight "

The sub program allows a user three tries to guess the correct answer to the question.
question = "Who is the Crown Prince of the Kingdom of Lucis?". The answer is "Noctis"

Frist set max_tries = 3. Then a loop is create to iterate three times only. 
For each  iteration, we ask the user for the answer (user input). 
Then based on the answer the user gives, we check to see if the user
input matches the answer. If so, print "Correct!" then terminate the loop
a break statement.

If the user could not guess the correct answer within the max_tries,
then print "You have used up your allotment of guesses.", the print 
"The correct answer is 'Noctis'"

"""
"""
import random
num = generate random number

if num is greater than 50,
    then the result will be "Emperor's Coin"
otherwise if num is > 40,
    then the result will be "Noble's Coin"
otherwise if num is > 30,
    then the result will be "Knight's Coin"
otherwise if num is > 20,
    then the result will be "Footman's Coin"
otherwise if num is > 10,
    then the result will be "Peasant's Coin"
otherwise
    the result will be "Chaos Coin"

loop tree times
    print the output (fate) to the user
    
main()

sub
    question = "Who is the Crown Prince of the Kingdom of Lucis?"
    answer = "Noctis"
    ask(question, answer)

ask
    tries = 0
    loop three times
        increment tries
        ask user input()
        check to see if user input us equal to answer
            if so, print "Correct" the exit loop
        if not correct
            print to user "You have used up your allotment of guesses."
            print the correct "The correct answer is 'Noctis'"

sub

"""
import random

def main():
    results = []

    for i in range(0, 3):
        results.append(spin())

    print("results", results) 
    Hero = The_Emperor_have_Arise(results)

    if (Hero):
        print("Hero's Coin acquire!")
    else:
        print("Chipped Heroo's Coin acquire!")

    option = input("You got enough Coin!")

    if option.lower() == "y" or option.lower() == "y = try again":
        main()

def spin():
    rand_num = random.randint(1, 15)
    output = ""
    if(rand_num > 50):
        output = "Emperor's Coin"
    elif(rand_num > 40):
        output = "Noble's Coin"
    elif(rand_num > 30):
        output = "Knight's Coin"
    elif(rand_num > 20):
        output = "Footman's Coin"
    elif(rand_num > 10):
        output = "Peasant's Coin"
    else:
        output = "Chaos Coin"

    print(output, end="")
    return output

def The_Emperor_have_Arise(results):
    return (results[0] == results[1] == results[2])
       
main()


def sub():
    question = "Who is the Crown Prince of the Kingdom of Lucis?"
    answer = "Noctis"
    ask(question, answer)

def ask(question, answer, max_tries=3):
    tries = 0
    ans = ""
    while tries < max_tries:
        tries = tries + 1
        print(tries)
        ans = input(question) #Noctis
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used up your allotment of guesses.")

sub()
