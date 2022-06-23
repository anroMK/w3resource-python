"""
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

"""
def sample_string():
    return "Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\t Up above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are"

#print(sample_string())



"""
2. Write a Python program to get the Python version you are using. Go to the editor
Click me to see the sample solution

"""


import sys
def version():
    return sys.version.split()[0]

#print(version())

"""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

"""
from datetime import datetime

def current_date_and_time():
    date = datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S")
    #return f"{date.year}:{date.month}:{date.day} {date.hour}:{date.minute}"

#print(current_date_and_time())

"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
Click me to see the sample solution

"""
from math import pi

def circle_area():
    radius = float(input("Enter the radius of circle: "))
    return pi * radius * radius

#print(circle_area())

"""
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor
Click me to see the sample solution

"""

def greetings():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return f"Hello {last_name} {first_name}!"

#print(greetings())

"""
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""

def seq_comma_separated_numbers():
    number = input("Enter sequence of comma separated numbers: ")
    print(f"List: {number.split(',')}")
    print(f"Tuple: {tuple(number.split(','))}")
    
#seq_comma_separated_numbers()

"""
7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java

"""

def extension():
    filename = input("Enter filename: ")
    return filename.split('.')[-1]

#print(extension())

"""
8. Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]

"""

def display_first_and_last(list):
    return f"{list[0]} {list[-1]}"

#print(display_first_and_last(["Red","Green","White" ,"Black"]))

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

"""
exam_st_date = (11, 12, 2014)

def extract_date(date):
    return f"{date[0]} / {date[1]} / {date[2]}"

#print(extract_date(exam_st_date))

"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615

"""

def sum_of_n():
    n = int(input("Enter the n: "))
    return n + int(f"{n}{n}") + int(f"{n}{n}{n}")

#print(sum_of_n())

"""
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.

"""

def print_documentation(name):
    print (name.__doc__)

#print_documentation(abs)
#print_documentation(max)

"""
13. Write a Python program to print the following 'here document'. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

"""

def print_here_document():
    return """a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""

#print(print_here_document())

"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

"""
from datetime import date
first = date(2014, 6, 2)
second = date(2014, 7, 11)

def numbers_of_days(first_date, second_date):
    return f"{abs(first - second).days} days"

#print(numbers_of_days(first,second))

"""
15. Write a Python program to get the volume of a sphere with radius 6.

"""

def sphere_volume():
    r = 6
    return 4/3 * pi * r ** 3

#print(sphere_volume())

"""
16. Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference. Go to the editor

"""

def difference():
    number = int(input("Enter the number: "))
    return 17  - number if number < 17 else 2 * abs(17 - number)

#print(difference())

"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

"""

def in_range():
    number = int(input("What number do you want to check?"))
    if 100 <= number <= 1000:
        return f"Number {number} is in the range 100-1000"
    elif 1000 < number <= 2000:
        return f"Number {number} is in the range 1001-2000"
    else:
        return f"Number {number} not in range."

#print(in_range())

"""
18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. Go to the editor
"""

def sum_of_three():
    numbers = input("Enter three numbers separated by comma: ").split(',')
    sum_of_three = sum([int(i) for i in numbers])
    if numbers.count(numbers[0]) == len(numbers):
        return 3 * sum_of_three
    else:
        return sum_of_three
        

#print(sum_of_three())

"""
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
"""

def add_is_to_the_top(str):
    return str if str[:2] == 'Is' and len(str) > 1 else 'Is' + str

#print(add_is_to_the_top('Array'))
#print(add_is_to_the_top('IsEmpty'))
#print(add_is_to_the_top(''))

"""
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 
"""

def larger_string(str, n):
    return str * n

#print(larger_string('abc', 2))
#print(larger_string('.py', 3))

"""
21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
"""

def even_or_odd():
    number = int(input('Enter an integer'))
    return f"{number} is even number" if number % 2 == 0 else f"{number} is odd number"

#print(even_or_odd())

"""
22. Write a Python program to count the number 4 in a given list.
"""

def list_count_four(lst):
    return lst.count(4)

#print(list_count_four([1, 4, 6, 7, 4]))
#print(list_count_four([1, 4, 6, 4, 7, 4]))

"""
23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
"""

def substring_copy(str,n):
    if len(str) < 2:
        return str * n
    else:
        return str[:2] * n

#print(substring_copy('abcdef', 2))
#print(substring_copy('p', 3))

"""
24. Write a Python program to test whether a passed letter is a vowel or not.
"""
    
def is_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return c.lower() in vowels

#print(is_vowel('c'))
#print(is_vowel('e'))
#print(is_vowel('C'))
#print(is_vowel('E'))

"""
25. Write a Python program to check whether a specified value is contained in a group of values.
"""
def part_of_list(lst, n):
    return n in lst


#print(part_of_list([1, 5, 8, 3], 3))
#print(part_of_list([5, 8, 3], -1))

"""
27. Write a Python program to concatenate all elements in a list into a string and return it.
"""

def concatenate_list_data(list):
    return ''.join([str(i) for i in list])


#print(concatenate_list_data([1, 5, 12, 2]))

"""
28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

"""

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

def even_numbers_till_break(numbers):
    try:
        index = numbers.index(237)
    except ValueError:
        return numbers
    return [i for i in numbers[:index] if i % 2 == 0]

#print(even_numbers_till_break(numbers))
#print(even_numbers_till_break([10,22,33,44,55]))

"""
29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def set_diff(set1, set2):
    return set1.difference(set2)

#print(set_diff(color_list_1, color_list_2))

"""
30. Write a Python program that will accept the base and height of a triangle and compute the area. 
"""

def triangle_area(base, heigh):
    return 0.5 * base * heigh

#print(triangle_area(20,40))

"""
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

def gcd(x, y):
    for i in range(min(x,y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i


#print("GCD of 12 & 17 =",gcd(12, 17))
#print("GCD of 4 & 6 =",gcd(4, 6))
#print("GCD of 336 & 360 =",gcd(336, 360))
#print("GCD of 12 & 12 =",gcd(12, 12))

"""
32. Write a Python program to get the least common multiple (LCM) of two positive integers.
"""

def lcm(x,y):
    if x == 0 or y == 0:
        return 0
    biger = max(x,y)
    lower = min(x, y)
    test = biger

    while test % lower != 0:
        test += biger
    
    return test

#print(lcm(4,6))
#print(lcm(15, 17))

"""
33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

def sum_three(x,y,z):
    if x==y or x==z or y==z:
        return 0
    return x + y + z

#print(sum_three(2, 1, 2))
#print(sum_three(3, 2, 2))
#print(sum_three(2, 2, 2))
#print(sum_three(1, 2, 3))

"""
34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""

def sum_of_two(x,y):
    return 20 if 15 <= x+y <= 20 else x + y


#print(sum_of_two(10, 6))
#print(sum_of_two(10, 2))
#print(sum_of_two(10, 12))
        
"""
35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

"""

def test_number5(x, y):
    return x == y or x + y == 5 or abs(x - y) == 5    

"""
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))
"""

"""
36. Write a Python program to add two objects if both objects are an integer type
"""

def add_if_int(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        return "Invalid input"

"""
print(add_if_int(10, 20))
print(add_if_int(10, 20.23))
print(add_if_int('5', 6))
print(add_if_int('5', '6'))
"""

"""
37. Write a Python program to display your details like name, age, address in three different lines.
"""

def personal_details(name, age, adress):
    return f"""name: {name}\nage: {age}\nadress: {adress}"""

#print(personal_details("Simon", 19, "Bangalore, Karnataka, India"))

"""
38. Write a Python program to solve (x + y) * (x + y). Go to the editor
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""

def calculate1(x,y):
    result = x*x + 2*x*y + y*y
    return f"({x} + {y}) ^ 2) = {result}"

#print(calculate1(4,3))

"""
40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""

def two_point_distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

"""
p1 = [4, 0]
p2 = [6, 6]
print(two_point_distance(p1, p2))
"""
"""
41. Write a Python program to check whether a file exists.
"""

def file_exist_check(name):
    try:
        with open(name) as f:
            print('File exist')
    except FileNotFoundError:
        print('File doesent exist')

#file_exist_check('basic.py')
#file_exist_check('xyz.py')

"""
42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""
import platform
import struct
def shell_mode():
    print(struct.calcsize("P") * 8)
    print(platform.architecture()[0])

#shell_mode()


"""
43. Write a Python program to get OS name, platform and release information.
"""

import os


def os_info():
    print("Name of the operatin system: ", os.name)
    print("Name of the OS system:",platform.system())
    print("Version of the operating system:",platform.release())
    


#os_info()

"""
44. Write a Python program to locate Python site-packages.
"""
import site
def site_packages_directory():
    return site.getsitepackages()

#print(site_packages_directory())


"""
46. Write a python program to get the path and name of the file that is currently executing.
"""

def current_path():
    return f"Current path: {os.getcwd()}"

print(current_path())

"""
47. Write a Python program to find out the number of CPUs using.
"""
import multiprocessing

def cpu_count():
    return multiprocessing.cpu_count()

#print(cpu_count())

"""
48. Write a Python program to parse a string to Float or Integer. 
"""

def float_and_int(str):
    print(f"float: {float(str)}")
    print(f"int: {int(float(str))}")

#float_and_int("246.246")

"""
49. Write a Python program to list all files in a directory in Python.
"""

def list_files():
    for i in os.listdir():
        print(i)

#list_files()

"""
53. Write a python program to access environment variables.
"""
#print(os.environ['PATH'])

"""
54. Write a Python program to get the current username.
"""

def current_username():
    print(os.getlogin())

#current_username()

"""

56. Write a Python program to get height and width of the console window.
"""

#print(os.get_terminal_size())
"""
57. Write a Python program to get execution time for a Python method.
"""

from datetime import datetime



def time_test():
    start = datetime.now()
    x= 0
    for i in range(10000000):
        x +=1
    end = datetime.now()
    return end - start

#print(time_test())

"""
58. Write a Python program to sum of the first n positive integers.

"""

def sum_of_int(n):
    return (n * (n + 1))/2

#print(sum_of_int(5))











