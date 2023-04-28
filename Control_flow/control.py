#1.Write a function that uses while, if and continue 
#statements to print all the even numbers between 0 and 50. 

def print_even_numbers():
    num = 0
    while num < 50:
        if num % 2 == 0:
            print(num)    
        num += 1
        continue    

#2.Write a function that takes an integer argument and prints "Prime" 
#if the number is prime, and "Not prime" if the number is not prime.

def is_prime(num):
    if num >= 1:
        for i in range(2,num):
            if(num % 2) == 0:
                print(num,"Is not prime")
        else:
            print(num,"is Prime")        
#3.Write a function that takes a list of integers as input and 
#prints the sum of all the even numbers in the list.

def sum_of_all_even(nums):
    w = 0
    for i in nums:
        total += i
    print(w)    
   

#4.Write a function that takes any two integers as input, and prints 
#the sum of all the numbers between the two integers (inclusive) that are divisible by 3.

def sum_of_all_numbers(n,m):
    number = []
    for x in range(n,m + 1):
        if x % 3 == 0:
            number.append(x)
    print(number)        

