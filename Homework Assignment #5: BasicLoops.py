"""
Homework Assignment #5: BasicLoops

Details:
 
You're about to do an assignment called "Fizz Buzz", which is one of the classic programming challenges. It is a favorite for interviewers, and a shocking number of job-applicants can't get it right. But you won't be one of those people. Here are the rules for the assignment (as specified by Imran Gory):

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".

The one hint you'll likely need is: 

There is a Python operator called "modulo", represented by the percentage sign (%) that gives you the remainder left over after division. So for example:

 6 % 3

Equals zero. Because after dividing 6 by 3, there is zero leftover. Whereas:

6 % 4

Equals 2. Because after dividing 6 by 4, there are 2 left over from the six.
If that was confusing, don't worry. It will make more sense as you use it. The point is: the modulo operator is useful for finding out if X is a multiple of Y. If it is, then X % Y will yield zero. Knowing this should help you complete this assignment without any issue.


Extra Credit:

Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime". You should print this whenever you encounter a number that is prime (divisible only by itself and one). As you implement this, don't worry about the efficiency of the algorithm you use to check for primes. It's okay for it to be slow.
"""


def is_prime(n):
    for p in range(2, n):
        if n % p == 0:
            return False
    return True
  



def fizzBuzz():
  print("__________")
  for i in range(1,101):
    if i > 2 and is_prime(i):
      print('Prime ',i)
      continue
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz ",i)
      continue
    if i % 3 == 0:
      print("Fizz ",i)
      continue
    if i % 5 == 0:
      print("Buzz ",i)
      continue
    else:
      print(i)

fizzBuzz()
