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