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
import re
from string import printable
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
















