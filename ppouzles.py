"""
1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Go to the editor
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
"""

def task1(list):
    return list.count(19) == 2 and list.count(5) >= 3

"""
print(task1([19,19,15,5,3,5,5,2]))
print(task1([19,15,15,5,3,3,5,2]))
print(task1([19,19,5,5,5,5,5]))
"""

"""
2. Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list. Go to the editor
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False
"""

def task2(list):
    return len(list) == 8 and list.count(list[4]) == 3

"""
print(task2([19, 19, 15, 5, 5, 5, 1, 2]))
print(task2([19, 15, 5, 7, 5, 5, 2]))
print(task2([11, 12, 14, 13, 14, 13, 15, 14]))
print(task2([19, 15, 11, 7, 5, 6, 2]))
"""

"""
3. Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
"""

def task3(number):
    return number > 4 ** 4 and number % 34 == 4

#print(task3(922))
#print(task3(914))
#print(task3(854))

"""
4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile. Go to the editor
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
"""
def task4(n):
    return  [n + i*2 for i in range(n)]
    
    

#print(task4(17))

"""
5. Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings. Go to the editor
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True
"""

def task5(list):
    return list[-2] in list[-1] and len(list) >= 2

#print(task5(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
#print(task5(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']))
#print(task5(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']))
#print(task5(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))

"""
6. Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return true or false. Go to the editor
Input:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
Output:
True
Input:
[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980]
Output:
False
"""
l1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
l2 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980]

def task6(list):
    return [*range(0,1000,10)] == list

#print(task6(l1))
#print(task6(l2))


"""
7. Write a Python program to check a given list of integers where the sum of the first i integers is i. Go to the editor
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
"""

def task7(list):
    return len(list) == sum(list)

#print(task7([0,1,2,3,4,5]))
#print(task7([1,1,1,1,1,1]))
#print(task7([2,2,2,2,2]))
#print(task7([0,2,0,2,0,2]))

"""
8. Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. Go to the editor
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]

"""
from multiprocessing.sharedctypes import Value
import re
from statistics import mean
from string import printable

from pyparsing import identchars
def task8(str):
    words = re.split(', | ', str)
    return(words)

#print(task8("W3resource Python, Exercises."))
#print(task8("The dance, held in the school gym, ended at midnight."))


"""
9. Write a Python program to find list integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries. Go to the editor
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False
"""

def task9(list):
    return all([list[i] != list[i+1] for i in range(len(list) - 1)]) and len(set(list)) == 4

    #len(set(list)) == 4

#print(task9([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))
#print(task9([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]))
#print(task9([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]))

"""
10. Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace. Go to the editor
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']
"""

def task10(list):
    output = []
    stack = []
    for i in list.replace(' ',''):
        stack.append(i)
        if stack.count('(') == stack.count(')'):
            output.append(''.join(stack))
            stack = []
    return output

#print(task10('( ()) ((()()())) (()) ()'))
#print(task10('() (( ( )() ( )) ) ( ())'))

"""
11. Write a Python program to find the indexes of numbers of a given list below a given threshold. Go to the editor
Input:
[(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
Output:
[0, 1, 2, 3, 7, 8, 9, 10]
Input:
[(10,(0, 12, 4, 3, 49, 9, 1, 5, 3))]
Output:
[0, 2, 3, 5, 6, 7, 8]
"""

def task11(n, list):
    return [i for i, val in enumerate(list) if val <= n]

#print(task11(100, (0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55)))
#print(task11(10, (0, 12, 4, 3, 49, 9, 1, 5, 3)))

"""
12. Write a Python program to check whether the given strings are palindromes or not. Return True, False. Go to the editor
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
"""


def task12(list):
    return [word == word[::-1] for word in list]

#print(task12(['palindrome', 'madamimadam', '', 'foo', 'eyes']))

"""
13. Write a Python program to find the strings in a given list, starting with a given prefix. Go to the editor
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']
"""

def task13(list, str):
    return [word for word in list if str == word[:2]]

#print(task13(('cat', 'car', 'fear', 'center'), 'ca'))
#print(task13(('cat', 'dog', 'shatter', 'donut', 'at', 'todo'),'do'))

"""
14. Write a Python program to find the lengths of a given list of non-empty strings. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]
"""

def task14(list):
    return [len(word) for word in list]
    #return [*map(len, list)]

#print(task14(['cat', 'car', 'fear', 'center']))
#print(task14(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))

"""
15. Write a Python program find the longest string of a given list of strings. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter

"""

def task15(list):
    current_longest = list[0]
    i = 0
    while i < len(list):
        if len(current_longest) < len(list[i]):
            current_longest = list[i]
        i += 1
    return current_longest
    #return max(list, key=len)



#print(task15(['cat', 'car', 'fear', 'center']))
#print(task15(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))

"""
16. Write a Python program find the strings in a given list containing a given substring. Go to the editor
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]
"""

def task16(substr, list):
    return [word for word in list if substr in word]

#print(task16('ca', ('cat', 'car', 'fear', 'center')))
#print(task16('o', ('cat', 'dog', 'shatter', 'donut', 'at', 'todo', '')))
#print(task16('oe', ('cat', 'dog', 'shatter', 'donut', 'at', 'todo', '')))

"""
17. Write a Python program to create string consisting of the non-negative integers up to n inclusive. Go to the editor
Input:
4
Output:
0 1 2 3 4
Input:
15
Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
"""

def task17(n):
    return ' '.join([str(i) for i in range(n+1)])

#print(task17(15))


"""
18. An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.
Write a Python program to find the indices of all occurrences of target in the uneven matrix. Go to the editor
Input:
[([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
Output:
[[0, 4], [1, 0], [1, 3], [4, 1]]
Input:
[([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
Output:
[[0, 1], [0, 3], [2, 2]]
"""



def task18(list, n):
    return [[i,j] for i, sublist in enumerate(list) for j, val in enumerate(sublist) if n in sublist and val == n]
    


#print(task18(([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]), 19))
#print(task18(([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2))

"""
19. Write a Python program to split a given string (s) into strings if there is a space in the string, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters with odd order (order of a = 0, b = 1, etc.) Go to the editor
Input:
a b c d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
a,b,c,d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
abcd
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['b', 'd']
"""

def task19(s):
    if ' ' in s:
        return s.split()
    if ',' in s:
        return s.split(',') 
    return [c for c in s if c.lower() if ord(c) % 2 == 0]


#print(task19('a b c d'))
#print(task19('a,b,c,d'))
#print(task19('abcd'))

"""
20. Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers. Go to the editor
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!
"""
"""
def task20(list):
    if list[0] > list[-1]:
        lst = [*range(list[0], list[-1]-1, -1)]
        if list == lst:
            return 'Decreasing.'
    if list[0] < list[-1]:
        lst = [*range(list[0], list[-1]+1, 1)]
        if list == lst:
            return 'Increasing.'
    return 'Not a monotonic sequence!'
"""


def task20(list):
    if all([list[i] > list[i + 1] for i in range(len(list)-1) ]):
        return 'Decreasing.'
    if all([list[i] < list[i + 1] for i in range(len(list)-1) ]):
        return 'Increasing.'
    return 'Not a monotonic sequence!'
    

#print(task20([1, 2, 3, 4, 5, 6]))
#print(task20([6, 5, 4, 3, 2, 1]))
#print(task20([19, 19, 5, 5, 5, 5, 5]))

"""
21. Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True or False. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]
"""

def task21(list):
    return [True if word[-2] == ' ' else False for word in list]

#print(task21(['cat', 'car', 'fear', 'center']))
#print(task21(['ca t', 'car', 'fea r', 'cente r']))

"""
22. Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string. Go to the editor
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
157
"""

def task22(s):
    return sum([ord(c) for c in s if c.isupper()])

#print(task22('PytHon ExerciSEs'))
#print(task22('JavaScript'))

"""
23. Write a Python program to find the indices for which the numbers in the list drops. Go to the editor
NOTE: You can detect multiple drops just by checking if nums[i] < nums[i-1]
Input:
[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Output:
[1, 4, 6, 8, 10, 11, 15, 16, 18]
Input:
[6, 5, 4, 3, 2, 1]
Output:
[1, 2, 3, 4, 5]
Input:
[1, 19, 5, 15, 5, 25, 5]
Output:
[0, 2, 4, 6]
"""

def task23(list):
    return [i for i in range(1,len(list),1) if list[i] < list[i-1]]

#print(task23([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]))

"""
24. Write a Python program to create a list whose ith element is the maximum of the first i elements from a input list. Go to the editor
Input:
[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Output:
[0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
Input:
[6, 5, 4, 3, 2, 1]
Output:
[6, 6, 6, 6, 6, 6]
Input:
[1, 19, 5, 15, 5, 25, 5]
Output:
[1, 19, 19, 19, 19, 25, 25]
"""
"""
def task24(list):
    result = [list[0]]
    for i in range(1, len(list)):
        if result[-1] > list[i]:
            result.append(result[-1])
        else:
            result.append(list[i])
    return result
"""

def task24(list):
    return [max(list[:i]) for i in range(1, len(list)+1)]

 

#print(task24([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]))
#print(task24([6, 5, 4, 3, 2, 1]))
#print(task24([1, 19, 5, 15, 5, 25, 5]))

"""
25. Write a Python program to find the XOR of two given strings interpreted as binary numbers. Go to the editor
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
"""


def task25(list):
    result = '0b'
    for i in range(len(list[0])):
        if list[0][i] == list[1][i]:
            result += '0'
        else: 
            result += '1'
    return result




#print(task25(['0001', '1011']))
#print(task25(['100011101100001', '100101100101110']))

"""
26. Write a Python program to find the largest number where commas or periods are decimal points. Go to the editor
Input:
['100', '102,1', '101.1']
Output:
102.1
"""


def task26(list):
    return max([float(i.replace(',','.')) for i in list])
    

#print(task26(['100', '102,1', '101.1']))


"""
27. Write a Python program to find x that minimizes mean squared deviation from a given a list of numbers. Go to the editor
Input:
[4, -5, 17, -9, 14, 108, -9]
Output:
17.142857142857142
Input:
[12, -2, 14, 3, -15, 10, -45, 3, 30]
Output:
1.1111111111111112

"""

def task27(list):
    return mean(list)

#print(task27([4, -5, 17, -9, 14, 108, -9]))
#print(task27([12, -2, 14, 3, -15, 10, -45, 3, 30]))

"""
28. Write a Python program to select a string from a given list of strings with the most unique characters. Go to the editor
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange
"""

def task28(list):
    dict = {i:len(set(i)) for i in list}
    return max(dict, key=lambda x: dict[x])
    #return  max(dict, key = dict.get)

#print(task28(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']))
#print(task28(['Green', 'Red', 'Orange', 'Yellow', '', 'White']))

"""
29. Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers. Go to the editor
Input:
[1, -4, 6, 7, 4]
Output:
[4, 1]
Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]
"""

def task29(list):
    for i in list:
        for j in list:
            if i == -j:
                return [list.index(i), list.index(j)]


#print(task29([1, -4, 6, 7, 4]))
#print(task29([1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]))

"""
30. Write a Python program to find the list of strings that has fewer total characters (including repetitions). Go to the editor
Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output:
['this', 'list', 'is', 'narrow']
Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']

"""

def task30(list1, list2):
    return list1 if len(''.join(list1).replace(' ', '')) < len(''.join(list2).replace(' ', '')) else list2
    

#print(task30(['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']))
#print(task30(['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']))













