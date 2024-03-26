# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:00:09 2024

@author: a2268
"""

#Challange
'''You have 100 cats. One day you decide to arrange all your cats in a giant circle. 
Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
The first round, you stop at every cat, placing a hat on each one.
The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
The third round, you only stop at every third cat(#3,#6,#9,#12, etc.).
You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.'''

number_of_cats = 100
cats_with_hats = []
number_of_laps = 100

# We want the laps to be from 1 to 100 instead of 0 to 99
for lap in range(1, number_of_laps + 1):
    for cat in range(1, number_of_cats + 1):
        # Only look at cats that are divisible by the lap
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)

print(cats_with_hats)

'''Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.'''
def capital_indexes(word):
    the_list = []
    for letter in range(0, len(word)):
        if word[letter] == word.upper()[letter]:
            the_list.append(letter)
    return the_list

capital_indexes("HeLLO ye KEw")

'''Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.'''
def mid(word):
    if len(word) % 2 == 1:
        return word[int(len(word)/2)]
    else:
        return ""

'''Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string "online" or "offline".
Your function should return the number of people who are online.'''

def online_count(dict):
    ppl_online = 0
    for ppl in dict:
        if dict[ppl] == "online":
            ppl_online = ppl_online + 1
    return ppl_online

my_dict = dict([("A", "online"), ("B", "offline"), ("C", "online"), ("D", "online")])
online_count(my_dict)

'''Define a function, random_number, that takes no parameters. 
The function must generate a random integer between 1 and 100, both inclusive, and return it.
Calling the function multiple times should (usually) return different numbers.'''

from random import randint 

def random_number():
    return randint(1, 100)
random_number()

'''Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.'''
def only_ints(a, b):
    return type(a) == int and type(b) == int

'''Define a function named double_letters that takes a single parameter. 
The parameter is a string. Your function must return True if there are 
two identical letters in a row in the string, and False otherwise.'''

def double_letters(word):
    for letter in range(0, len(word)-1):
        while word[letter] == word[letter+1]:
            return True
    return False

double_letters("fgdfgdedff")

'''
Write a function named add_dots that takes a string and adds "." in between each letter. 
For example, calling add_dots("test") should return the string "t.e.s.t".
Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 
For example, calling remove_dots("t.e.s.t") should return "test".'''

def add_dots(word):
    new_word = ".".join(word)
    return new_word
add_dots("word")

def remove_dots(word):
    new_word = word.replace(".", "")
    return new_word
remove_dots("w.o.r.d")

def remove_dots(word):
    new_word = ""
    for letter in range(0,len(word)):
        if word[letter] != ".":
            new_word = new_word + word[letter]
    return new_word

remove_dots("h.i.g.h.w.a.y t.o h.e.l.l")

'''Define a function named count that takes a single parameter. 
The parameter is a string. The string will contain a single word divided into syllables by hyphens.
Your function should count the number of syllables and return it.'''

def count(word):
    syl = 1
    for letter in word:
        if letter == "-":
            syl = syl + 1
    return syl

def count(word):
    return word.count("-") + 1

def count(word):
    return len(word.split("-"))

count("de-mo-nic")

'''Write a function named is_anagram that takes two strings as its parameters. 
Your function should return True if the strings are anagrams, and False otherwise.'''

def is_anagram(word1, word2):
    for letter in word1:
        if word1.count(letter) != word2.count(letter):
            return False
    return True

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

is_anagram("word3", "word4")

'''Write a function that takes a list of lists and flattens it into a one-dimensional list.
Name your function flatten. It should take a single parameter and return a list.'''

def flatten(list_list):
    new_list = []
    for element in list_list:
        if type(element) == list:
            for index in range(0, len(element)):
                new_list.append(element[index])
        else:
            new_list.append(element)
    return new_list

def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]

flatten([[1, 2], [[3,5], 4]])

'''Define a function named largest_difference that takes a list of numbers as its only parameter.
Your function should compute and return the difference between the largest and smallest number in the list.'''

def largest_difference(num_list):
    return max(num_list) - min(num_list)

largest_difference([1, 2, 65])

'''Define a function named div_3 that returns True if its single integer parameter is divisible by 3 
and False otherwise.'''

def div_3(num):
    return num % 3 == 0

div_3(368)

'''
1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C
Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). 
Name your function get_row_col; it should take a single parameter
which is a string of length 2 consisting of an uppercase letter and a digit.'''

def get_row_col(word):
    translate = {"A": 0, "B": 1, "C": 2}
    col = translate[word[0]]
    row = int(word[1]) - 1    
    return (row, col)

get_row_col("B3")

'''Write a function named palindrome that takes a single string as its parameter. 
Your function should return True if the string is a palindrome, and False otherwise.'''

def palindrome(word):
    return word == word[::-1]

palindrome("wow")

'''Define a function named up_down that takes a single number as its parameter. 
Your function return a tuple containing two numbers; 
the first should be one lower than the parameter, and the second should be one higher.'''

def up_down(num):
    return (num - 1, num + 1)

up_down(4)

'''Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. 
Your code should find the biggest number of consecutive zeros in the string.'''

def consecutive_zeros(string):
    binary_list = string.split('1')
    biggest_number = max(map(len, binary_list)) #map() applies a function to the series inside an object 
    return biggest_number

def consecutive_zeros(string):
    return max([len(string) for string in string.split("1")])

print(consecutive_zeros("10011010000110"))

'''Define a function named all_equal that takes a list and checks whether all elements in the list are the same.'''

def all_equal(the_list):
    return [the_list[0]] * len(the_list) == the_list

def all_equal(the_list):
    return len(set(the_list)) == 1 or len(set(the_list))== 0

all_equal(["a", "a", "a"])
all_equal([])

'''Define a function named triple_and that takes three parameters and 
returns True only if they are all True and False otherwise.'''

def triple_and(a, b, c):
    return a and b and c

triple_and(1, 1, 1)

''' Define a function named convert that takes a list of numbers as its only parameter and returns a list of
 each number converted to a string.What makes this tricky is that your function body must only contain a single line of code. '''

def convert(the_list):
    return [str(element) for element in the_list]

convert([2,4,"wat"])

''' The built-in zip function "zips" two lists. Write your own implementation of this function.
Define a function named zap. The function takes two parameters, a and b. These are lists.
Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
You may assume a and b have equal lengths.'''

def zap(list1, list2):
    new_list = []
    for i in range(0,len(list1)):
        new_list.append((list1[i], list2[i]))
    return new_list

def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]

zap([0, 1, 2, 3],
    [5, 6, 7, 8])

'''Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.'''

def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True

'''Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
Your function must return whether n is exclusively in list1 or list2.
If n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.'''

def list_xor(n, list1, list2):
    if n in list1 and n not in list2:
        return True
    if n in list2 and n not in list1:
        return True
    return False

def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)  # ^ exclusive or operator

list_xor(1, [1, 2, 3], [4, 5, 6])
list_xor(1, [0, 2, 3], [1, 5, 6]) 
list_xor(1, [1, 2, 3], [1, 5, 6])
list_xor(1, [0, 0, 0], [4, 5, 6]) 

'''Define a function param_count that takes a variable number of parameters. 
The function should return the number of arguments it was called with.'''

def param_count(*stuff):
    arg = 0
    for i in range(len(stuff)):
        if type(stuff[i]) in [int, str, float, bool, dict, list, set, tuple]:
            arg += 1
    return arg
        
def param_count(*args):
    return len(args)

param_count(2, 4, "a", 2.0, False, [2,4], {"Key1": 2, "Key2": 4}, (2,4))
param_count(2, 4, 2, False)

'''Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.

1234567
"765,432,1"
"1,234,567" 
'''

def format_number(num):
    new_num = ""
    for i in range(len(str(num))):
        if i == len(str(num)) - 1:
           new_num += str(num)[::-1][i] 
        elif i % 3 == 2 or i == 2:
            new_num += str(num)[::-1][i] + ","
        else:
            new_num += str(num)[::-1][i]
    return new_num[::-1]

def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

def format_number(n):
    return "{:,}".format(n)

format_number(100001234200)

'''We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?'''


for h in range(35):
    if ((94 - 4 * h)/2) == (35 - h):
        rabbit = h
        chicken = 35 - rabbit
print(f"There are {rabbit} rabbits ")
print(f"There are {chicken} chickens ")

'''write a program which prints all permutations of [1,2,3]'''
import itertools
print(list(itertools.permutations([1,2,3])))

'''Write a program which accepts a string from console and print the characters that have even indexes.'''
def even_index(word):
    new_word = ""
    for i in range(len(word)):
        if (i + 1) % 2 == 1:
            new_word = new_word + str(word[i])
    return new_word

def even_index(word):
    return word[::2]

even_index("1n2j3k4h5g6y")

'''With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list 
after removing all duplicate values with original order reserved.'''

def remove_dup(the_list):
    new_list = []
    already = set()
    for item in the_list:
        if item not in already:
            already.add(item)
            new_list.append(item)
    return new_list[::-1]

remove_dup([1,3,5,3,5,7,8,4,1,7])

'''write a program which count and print the numbers of each character in a string input by console.'''

def count_ele(word):
    li = []
    seen = set()
    for i in range(len(word)):
        if word[i] not in seen:
            li.append(word[i])
            seen.add(word[i])
    for e in range(len(li)):
        print(f"{li[e]} , {word.count(li[e])}")

count_ele("opopoergfdgfd")

'''With two given lists, write a program to make a list whose elements are intersection of the above given lists.'''
def in_lists(list1, list2):
    new_list = []
    list1 = list(set(list1))
    for i in range(len(list1)):
        if list1[i] in list2:
            new_list.append(list1[i])
    return new_list

in_lists([0,1,2,3,4,5,0,5,1], [0,1,5,6,7,8])

'''write a program to print the list after removing the 1st,5th,6th elements'''
def remove_th(the_list):
    return [x for (i, x) in enumerate(the_list) if i not in (0, 4, 5)]

remove_th([1,4,5,8,9,0,6,4])

'''write a program to generate all sentences where subject is in ["I", "You"] and verb 
is in ["Play", "Love"] and the object is in ["Hockey","Football"].'''

subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey","Football"]

new_list = []
for s in range(len(subject)):
    for v in range(len(verb)):
        for o in range(len(objects)):
            new_list.append([subject[s],verb[v],objects[o]])
print(new_list)

'''Write a program which can map() and filter() to make a list whose elements 
are square of even number in [1,2,3,4,5,6,7,8,9,10].'''

li = [1,2,3,4,5,6,7,8,9,10]
even_squared = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, li))
print(list(even_squared))

'''Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).'''
def n_sum(num):
    new_num = 0
    for i in range(1,num+1):
            new_num += i/(i+1)
    return new_num

n_sum(5)

'''The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Write a program to compute the value of f(n) with a given n input by console.'''

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2) 

f(6)

'''write a program using list comprehension to print the Fibonacci Sequence 
in comma separated form with a given n input by console.'''

def fibo_list(n):
    li = []
    for i in range(n+1):
        li.append(f(i))
    return li

fibo_list(7)

'''write a program using generator to print the even numbers between 0 and n in comma 
separated form while n is input by console.'''

def even(n):
    li = []
    for i in range(int(n/2) + 1):
        li.append(i*2)
    return li

even(9)

'''evaluate string expressions'''
eval("38%7")

'''write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.'''
import random
random.sample([i for i in range(100, 201) if i%2 == 0],5)

'''write a program to shuffle and print the list [3,6,7,8].'''
from random import shuffle
li = [3,6,7,8]
shuffle(li)

'''A website requires the users to input username and password to register. Write a program to check the 
validity of password input by users. Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 

Your program should accept a sequence of comma separated passwords and will check them according to the 
above criteria. Passwords that match the criteria are to be printed, each separated by a comma. 
Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 
Then, the output of the program should be: ABd1234@1'''

import re
value = []
items=input().split(',')
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))


















